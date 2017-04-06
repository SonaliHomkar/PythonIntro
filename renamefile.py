import os,sys
import re

path = "I:\Sonali Git Hub\songsHindi"
dirs = os.listdir(path)

for file in dirs : 
    #print (path + "\\" + dirs[0])
    oldfile = os.path.join(path,file)
    newfile = os.path.join(path,re.sub(r'\b\d+\b',"",file))
    os.rename( oldfile,newfile)   
    print("newfile  " + newfile)

     
