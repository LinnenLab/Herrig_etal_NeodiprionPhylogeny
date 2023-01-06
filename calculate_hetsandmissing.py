import re
from re import findall
#import OS

infile=open('regions.txt','r')
content=infile.read()
infile.close()

regions=findall('[^\n]+',content)

hets=open('hets_1mb.matrix','w')
missing=open('missing_1mb.matrix','w')
started='no'

header='location'

for region in regions:
    infile=open('interior_window1000000/'+region+'.fa','r')
    currenthet=region
    currentmissing=region
    for line in infile:
        if '>' in line:
            if started == 'no':
                name=line.replace('\n','')
                header=header+'\t'+name
        else:
            try:
                Ns=findall('N',line)
                IUPAC=findall('[^A^C^G^T^N]',line)
                sites=findall('[A-Z]',line)
                currenthet=currenthet+'\t'+str(float(len(IUPAC))/float(len(sites)))
                currentmissing=currentmissing+'\t'+str(float(len(Ns))/float(len(sites)))
            except:
                print('interior_window1000000/'+region+'.fa',name)
    if started=='no':
        started='yes'
        hets.write(header+'\n')
        missing.write(header+'\n')
        print(len(Ns))
        print(len(IUPAC))
        print(len(sites))
    hets.write(currenthet+'\n')
    missing.write(currentmissing+'\n')
        
    infile.close()
    
hets.close()
missing.close()





            
            
            
        
        
    
