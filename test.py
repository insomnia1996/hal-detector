import numpy as np
import os
import re
f=np.load("apimatrix1.npy")

for i in range(len(f)):
    for j in range(len(f[i])):
        print(f[i][j])
        print()
    
        
    
