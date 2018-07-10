import numpy as np

with open('pred_1.txt') as f:
    #w = [int(x) for x in next(f).split()] # read first line
    array = []
    for line in f: # read rest of lines
        w = [int(x) for x in line.split()]
        #print(w)
        array.extend(w)
print(len(array))

with open('pred_2.txt') as f:
    #w = [int(x) for x in next(f).split()] # read first line
    array2 = []
    for line in f: # read rest of lines
        w = [int(x) for x in line.split()]
        #print(w)
        array2.extend(w)
print(len(array2))

unique, counts = np.unique(array, return_counts=True)
print(np.asarray((unique, counts)).T)

unique, counts = np.unique(array2, return_counts=True)
print(np.asarray((unique, counts)).T)
