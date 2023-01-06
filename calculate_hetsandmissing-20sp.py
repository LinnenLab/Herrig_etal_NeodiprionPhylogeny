import re
from re import findall
import sys

infile=open('regions.txt','r')
content=infile.read()
infile.close()

regions=findall('[^\n]+',content)
size=sys.argv[1]


hets=open('20sp_hets_'+size+'kb.matrix','w')
missing=open('20sp_missing_'+size+'kb.matrix','w')
started='no'

header='location'

for region in regions:
    infile=open('20species_window'+size+'000/'+region+'.fa','r')
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
                print('20species_window'+size+'000/'+region+'.fa',name)
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
