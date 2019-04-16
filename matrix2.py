import re
import os
import numpy as np
apilist=np.load("apilist.npy")
paclist=[]
apiofpac=[]
for i in range (len(apilist)):
    paclist.append(apilist[i].split(";->")[0])
    apiofpac.append(apilist[i].split(";->")[1])
matrix=np.zeros((len(apilist),len(apilist)),dtype=np.int)
for i in range (len(apilist)):
    for j in range( len(apilist)):
        if (paclist[i]==paclist[j]):
            matrix[i][j]=1
np.save("matrix2.npy",matrix)
