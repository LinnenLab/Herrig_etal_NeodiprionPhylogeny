import re
from re import findall
import sys

infile=open('filteredinfo-20sp.matrix','r')
content=infile.read()
infile.close()
regions=findall('Chromosome'+'[\S]+',content)


print('Calculating BSs and Filtering!')
outfile=open('bootstrapaves.txt','w')
for region in regions:
    infile=open('20species_window5000/'+region+'.fa.treefile','r')
    content=infile.read()
    infile.close()
    bootstraps=findall('[0-9\.]+'+'/',content)
    bss=[]
    try:
        for bootstrap in bootstraps:
            bss.append(float(bootstrap.replace('/','')))
        avebootstrap=sum(bss)/len(bss)
        outfile.write(region+'\t'+str(avebootstrap)+'\n')

    except:
        print('error with '+region)
outfile.close()
