import re
import os
import numpy as np

invokelist=np.load("invokelist.npy")
apilist=np.load("apilist.npy")
length=len(apilist)
matrix3=np.zeros((length,length),dtype=np.int)
for i in range(length):
    for j in range(length):
        if (invokelist[i]==invokelist[j]):
            matrix3[i][j]=1
np.save("matrix3.npy",matrix3)
