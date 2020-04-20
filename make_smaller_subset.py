import utils
import os
import random
import subprocess

maindir = "" #give proper path to the complete dataset

if not os.path.isdir(maindir):
    print ('ERROR: directory',maindir,'does not exists.')
#check path to make sure

allh5 = utils.get_all_files(maindir,ext='.h5')
#check the lenght of the full directory
len(allh5)

allh5[:5]
#check first 5 rows
random.shuffle(allh5)
allh5[:5]
#check first 5 rows and make sure that they have been shuffled
split_data = allh5[:int((len(allh5)+1)*.20)]

#copying the files from the lsit of filepaths iteratively
for i in split_data:
    list_files = subprocess.run(["aws","s3","cp",i,"whatever_bucket_directory"])
    print(list_files.returncode)