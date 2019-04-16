import re
import os
import numpy as np

apilist=[]
invokelist=[]
methodapilist=[]
pathlist=[]

pattern=re.compile(r'\S*.smali')
pattern2=re.compile(r'\S*.apk')
pattern3=re.compile(r'[0-9a-z]*')
tstptn=re.compile(r'PGRenderer.smali')
for root,dirs,files in os.walk("."):
    for name in files:
        if pattern.match(name):
            f=open(os.path.join(root,name),'r',encoding="UTF-8")
            while True:
                line=f.readline()
                if line:
                    if (line[0:7]==".method"):
                        methodname=line[8:].split('(')[0];
                        methodapilist.append([])
                        #print (methodname)
                        while True:
                            line2=f.readline()
                            
                            if (line2!=".end method\n"):
                                if (line2.find("invoke-")!=-1):#获取api名
                                    invokename=re.split(r' |\t|\n|/',line2)[4]
                                    #print(invokename)
                                    apiname=line2.split(",")[-1][:-1]
                                    methodapilist[-1].append(apiname)
                                    #methodapilist.append(apiname)
                                    #print (apiname)
                                    if apiname not in apilist:
                                        apilist.append(apiname)
                                        invokelist.append(invokename)
                                        pathlist.append(os.path.join(root,name))

                                        
                            else:
                                #print (line2)
                                break#这里获取到整个method中的invoke-method
                        #print("end method!")
                else:
                    #print ("finish one file!")
                    break
print ("finish!")
#randomly select useful api from apilist
newapilist=[]
newinvokelist=[]
newpathlist=[]
for i in range(40):
    for j in range(10):
        newapilist.append(apilist[1000*i+j])
        newinvokelist.append(invokelist[1000*i+j])
        newpathlist.append(pathlist[1000*i+j])



#starting to make matrix from codeapimatrix content above
#处理method中提取的api内容并将其变为矩阵
length=len(newapilist)
print (length)
apimatrix=np.zeros((length,length),dtype=np.int)
for i in range(length):
    for j in range(length):
        for method in methodapilist:
            if ((newapilist[i] in method) and (newapilist[j] in method)):
                apimatrix[i][j]=1
                break
        #print("--------")
print("matrix finish")

np.save("apimatrix1.npy",apimatrix)
np.save("apilist.npy",newapilist)
np.save("invokelist.npy",newinvokelist)
np.save("pathlist.npy",newpathlist)
