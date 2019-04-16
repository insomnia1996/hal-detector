import re
import os
import numpy as np
apilist=np.load("apilist.npy")
pathlist=np.load("pathlist.npy")
apklist=[]

pattern=re.compile(r'\S*.smali')
pattern2=re.compile(r'\S*.apk')
pattern3=re.compile(r'[0-9a-z]*')
tstptn=re.compile(r'PGRenderer.smali')
for root,dirs,files in os.walk("."):
    if (root==".\\normal"):
        for name in files:
            if pattern2.match(name):
                apklist.append(os.path.join(root,name[:-4]))
    if (root==".\\malware"):
        for name in files:
            if pattern3.match(name):
                apklist.append(os.path.join(root,name+".out"))
appapimatrix=np.zeros((len(apklist),len(apilist)),dtype=np.int)                
length=len(apilist)
for i in range(length):
    for j in range(len(apklist)):
        print(pathlist[i])
        print(apklist[j])
        if (pathlist[i].find(apklist[j]) !=-1):
            appapimatrix[j][i]=1

np.save("appmatrix.npy",appapimatrix)
        
