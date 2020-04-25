#!/bin/bash

# modified and adapted from https://raw.githubusercontent.com/dask/dask-yarn/master/deployment_resources/aws-emr/bootstrap-dask
set -x -e


start_time="$(date -u +%s.%N)"

IS_MASTER=false
if grep isMaster /mnt/var/lib/info/instance.json | grep true;
then
    IS_MASTER=true
fi

# -----------------------------------------------------------------------------
# 1. Install Miniconda on master and server and add to path
# -----------------------------------------------------------------------------
echo "Installing Miniconda"
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh
bash /tmp/miniconda.sh -b -p $HOME/miniconda
rm /tmp/miniconda.sh
echo -e '\nexport PATH=$HOME/miniconda/bin:$PATH' >> $HOME/.bashrc
source $HOME/.bashrc
conda update conda -y


# -----------------------------------------------------------------------------
# 2. Install packages to use in worker and packaged environment
#
# -----------------------------------------------------------------------------
echo "Installing common Python pacakges on master and workers"
conda install \
-c defaults \
-c conda-forge \
-y \
dask-yarn>=0.7.0 \
pyarrow \
s3fs \
bokeh \
conda-pack \
tornado=5



# -----------------------------------------------------------------------------
# 3. List all packages in the worker nodes
# -----------------------------------------------------------------------------
if [ "$IS_MASTER" = false ]; then
    echo "Python packages installed in worker nodes:"
    conda list
fi

# -----------------------------------------------------------------------------
# 4. Configure Dask
#
# This isn't necessary, but for this particular bootstrap script it will make a
# few things easier:
#
# - Configure the cluster's dashboard link to show the proxied version through
#   jupyter nbserverproxy. This allows access to the dashboard with only an ssh
#   tunnel to the notebook.
#
# - Specify the pre-packaged python environment, so users don't have to
#
# - Specify the location of the native libhdfs library so pyarrow can find it
#   on the workers and the client (if submitting applications).
# ------------------------------------------------------------------------------
if [ "$IS_MASTER" = true ]; then


# -----------------------------------------------------------------------------
# 5. Package the environment to be distributed to worker nodes
# -----------------------------------------------------------------------------
echo "Packaging environment from master (for Dask)"
conda pack -q -o $HOME/environment.tar.gz


echo "Configuring Dask"
mkdir -p $HOME/.config/dask
cat <<EOT >> $HOME/.config/dask/config.yaml
distributed:
  dashboard:
    link: "/proxy/{port}/status"
yarn:
  environment: /home/hadoop/environment.tar.gz
  deploy-mode: local
  worker:
    env:
      ARROW_LIBHDFS_DIR: /usr/lib/hadoop/lib/native/
  client:
    env:
      ARROW_LIBHDFS_DIR: /usr/lib/hadoop/lib/native/
EOT
# Also set ARROW_LIBHDFS_DIR in ~/.bashrc so it's set for the local user
echo -e '\nexport ARROW_LIBHDFS_DIR=/usr/lib/hadoop/lib/native' >> $HOME/.bashrc


# -----------------------------------------------------------------------------
# 6. Install additional Python libraries on Master node
#
# -----------------------------------------------------------------------------
sudo yum install -y git libcurl-devel
echo "Installing Master node Python libraries"
conda install \
-c defaults \
-c conda-forge \
-y \
notebook \
ipywidgets \
jupyter-server-proxy \
findspark \
matplotlib \
jupyterlab \
scikit-learn \
nltk \
scipy \
beautifulsoup4 \
nose \
lxml \
hdf5 \
seaborn \
pyspark \
pytables \
h5py

conda install -c johnsnowlabs -y spark-nlp=2.4.5



# -----------------------------------------------------------------------------
# 7. List all packages in the client environment
# -----------------------------------------------------------------------------
echo "Python packages installed in master node."
conda list

# -----------------------------------------------------------------------------
# 8. Configure Jupyter Notebook
# -----------------------------------------------------------------------------
echo "Configuring Jupyter Lab for port 8765, no password and no token"
mkdir -p $HOME/.jupyter

cat <<EOF >> $HOME/.jupyter/jupyter_notebook_config.py
c.NotebookApp.open_browser = False
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = 8765
c.NotebookApp.token = ''
EOF

# -----------------------------------------------------------------------------
# 9. Define an upstart service for the Jupyter Notebook Server
# -----------------------------------------------------------------------------
echo "Configuring Jupyter Lab Upstart Service"
cat <<EOF > /tmp/jupyter-lab.conf
description "Jupyter Lab Server"
start on runlevel [2345]
stop on runlevel [016]
respawn
respawn limit unlimited
exec su - hadoop -c "jupyter lab" >> /var/log/jupyter-lab.log 2>&1
EOF
sudo mv /tmp/jupyter-lab.conf /etc/init/

# -----------------------------------------------------------------------------
# 10. Start the Jupyter Notebook Server
# -----------------------------------------------------------------------------
echo "Starting Jupyter Notebook Server"
sudo initctl reload-configuration
sudo initctl start jupyter-lab


# -----------------------------------------------------------------------------
# 11. Modify login message
# -----------------------------------------------------------------------------

sudo tee -a /etc/profile.d/motd.sh << END
echo "Your Big Data Cluster is Ready! You are logged into the master node.";
echo "                                                                    ";
echo "Git is installed and Jupyter Lab is running in port 8765. You are   ";
echo "now able to clone multiple repositories and see them in a single    ";
echo "Jupyter session. There is not need to manually run a script.        ";
echo "                                                                    ";
echo "To access Jupyter make sure you connect to the cluster with port    ";
echo "forwarding, and ssh-agent if necessary. If you did not, type exit   ";
echo "to log out and then log back in:                                    ";
echo "                                                                    ";
echo "ssh -A -L8765:localhost:8765 hadoop@...                             ";
echo "and then open a web browser on your laptop and go to                ";
echo "http://localhost:8765                                               ";
echo "                                                                    ";
echo "Remember to configure your git settings (every time you create a    ";
echo "cluster. You only need to do this once.                             ";
echo "                                                                    ";
echo "git config --global user.name \"[[your name]]\"                       ";
echo "git config --global user.email \"[[your email]]\"                       ";
echo "                                                                    ";
echo "Have fun!                                                           ";
echo "--------------------------------------------------------------------";
END

# -----------------------------------------------------------------------------
# 12. Download and unpack graphframes jar
# -----------------------------------------------------------------------------
echo "Downloading and unpacking graphframes"
cd ~
wget http://dl.bintray.com/spark-packages/maven/graphframes/graphframes/0.7.0-spark2.4-s_2.11/graphframes-0.7.0-spark2.4-s_2.11.jar
jar xf graphframes-0.7.0-spark2.4-s_2.11.jar

fi

end_time="$(date -u +%s.%N)"
elapsed="$(bc <<<"scale=2;($end_time-$start_time)/60")"
echo "Bootstrap took $elapsed minutes"