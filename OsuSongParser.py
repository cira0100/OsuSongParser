import re
import os
import shutil
regexComp=re.compile(r'^[0-9]*')
regexMp3=re.compile(r'\.mp3$')
cwd = os.getcwd()
sum=0
s=input("type path to Osu Songs \n")
for filename in os.listdir(s):
    sum=sum+1
for filename in os.listdir(s):
    test=regexComp.search(filename)
    songName=filename[len(test.group(0))+1:]+".mp3"
    path=os.path.join(s,filename)
    sum=sum-1
    print("Files left ........ "+str(sum))
    for name in os.listdir(path):
        if(regexMp3.search(name)):
            shutil.copy(os.path.join(path,name),cwd)
            os.rename(os.path.join(cwd,name),os.path.join(cwd,songName))
            break
            
print("Done")




