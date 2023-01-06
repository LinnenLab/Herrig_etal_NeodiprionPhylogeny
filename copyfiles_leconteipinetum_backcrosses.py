import re
from re import findall
import shutil

infile=open('backcrossreadlist.txt','r')
LBXoutfile=open('LBXlist.txt','w')
PBXoutfile=open('PBXlist.txt','w')
for line in infile:
    name=line.replace('\n','')
    if 'FEB' in line:
        newPath = shutil.copy('backcrossreads/'+name,'data/LBXreads/')
        LBXoutfile.write('data/LBXreads/'+line)
    elif 'KMM' in line:
        newPath = shutil.copy('backcrossreads/'+name,'data/LBXreads/')
        LBXoutfile.write('data/LBXreads/'+line)
    elif 'RX013xINV7' in line:
        newPath = shutil.copy('backcrossreads/'+name,'data/LBXreads/')
        LBXoutfile.write('data/LBXreads/'+line)
    elif 'LBX' in line:
        newPath = shutil.copy('backcrossreads/'+name,'data/LBXreads/')
        LBXoutfile.write('data/LBXreads/'+line)
    elif 'RX014XPX' in line:
        newPath = shutil.copy('backcrossreads/'+name,'data/PBXreads/')
        PBXoutfile.write('data/PBXreads/'+line)
    elif 'PBX' in line:
        newPath = shutil.copy('backcrossreads/'+name,'data/PBXreads/')
        PBXoutfile.write('data/PBXreads/'+line)
    else:
        print(name)
infile.close()
print('done')
    
        
