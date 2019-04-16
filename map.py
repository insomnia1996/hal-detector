import re
import os
import numpy as np
a=np.load("appmatrix.npy")
p=np.load("matrix2.npy")
b=np.load("apimatrix1.npy")
i=np.load("matrix3.npy")
length=len(b)
print(length)

for n in range(2):
        newmat=[]
        newmat.extend(a[n])
        newmat.extend(np.dot(a[n],b))
        newmat.extend(np.dot(a[n],p))
        newmat.extend(np.dot(a[n],i))
        newmat.extend(np.dot(a[n],np.dot(b,p)))
        newmat.extend(np.dot(a[n],np.dot(p,b)))
        newmat.extend(np.dot(a[n],np.dot(b,i)))
        newmat.extend(np.dot(a[n],np.dot(i,b)))
        newmat.extend(np.dot(a[n],np.dot(p,i)))
        newmat.extend(np.dot(a[n],np.dot(i,p)))
        newmat.extend(np.dot(np.dot(a[n],b),np.dot(p,i)))
        newmat.extend(np.dot(np.dot(a[n],p),np.dot(b,i)))
        newmat.extend(np.dot(np.dot(a[n],b),np.dot(i,p)))
        newmat.extend(np.dot(np.dot(a[n],i),np.dot(b,p)))
        newmat.extend(np.dot(np.dot(a[n],i),np.dot(p,b)))
        newmat.extend(np.dot(np.dot(a[n],p),np.dot(i,b)))
        print(len(newmat))
        mat=np.array(newmat)
        mat.reshape([16,length],order='C')
        np.save("mat"+str(n)+".npy",mat)

