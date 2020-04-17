import os
import sys
import hdf5_getters
import numpy as np
import utils
import pandas as pd
import time


def die_with_usage():
    sys.exit(0)


if __name__ == '__main__':
    #not enough arguments
    if len(sys.argv) < 2:
        die_with_usage()

    # flags: to get all possible attributes instead of a specific one
    summary = False
    while True:
        if sys.argv[1] == '-summary':
            summary = True
        else:
            break
        sys.argv.pop(1)

    songidx = 0
    onegetter = ''
    # params
    maindir = sys.argv[1]
    #output = sys.argv[2]
    t1 = time.time()
    # sanity checks
    if not os.path.isdir(maindir):
        print ('ERROR: directory',maindir,'does not exists.')
        sys.exit(0)

    # get all h5 files
    allh5 = utils.get_all_files(maindir,ext='.h5')
    #print ('found',len(allh5),'H5 files.')
    
    # get all getters
    getters = filter(lambda x: x[:4] == 'get_', hdf5_getters.__dict__.keys())
    getters = list(getters)
    getters.remove("get_num_songs") # special case
    if onegetter == 'num_songs' or onegetter == 'get_num_songs':
        getters = []
    elif onegetter != '':
        if onegetter[:4] != 'get_':
            onegetter = 'get_' + onegetter
        try:
            getters.index(onegetter)
        except ValueError:
            print('ERROR: getter requested:',onegetter,'does not exist.')
            sys.exit(0)
        getters = [onegetter]
    getters = np.sort(getters)
    attribute_list = []
    #creating the dataframe
    for getter in getters:
        attribute_list.append(getter[4:])
    print('no. of attributes = ',len(attribute_list))
    subset_df = pd.DataFrame(columns=attribute_list)
    #print(subset_df)

    for i in range(0,len(allh5)):
        h5 = hdf5_getters.open_h5_file_read(allh5[i])
        numSongs = hdf5_getters.get_num_songs(h5)
        # print them
        for getter in getters:
            try:
                res = hdf5_getters.__getattribute__(getter)(h5,songidx)
            except AttributeError:
                if summary:
                    continue
                else:
                    #print(e)
                    print('forgot -summary flag? specified wrong getter?')
            if res.__class__.__name__ == 'ndarray':
                #print(getter[4:]+": shape =",res.shape)
                subset_df.loc[i,getter[4:]] = res.shape
            else:
                #print(getter[4:]+":",res)
                subset_df.loc[i,getter[4:]] = res
    
        # done
        #print('DONE, showed song',songidx,'/',numSongs-1,'in file:',hdf5path)
        h5.close()
    stimelength = str(datetime.timedelta(seconds=time.time()-t1))
    print ('Aggregated',len(allh5),'files in:',stimelength)
    subset_df.to_csv(r'C:\Users\subha\Documents\Georgetown\Spring 2020\Massive Data Fundamentals\project\subset-compiled.csv', 
                     index=False, header=True)