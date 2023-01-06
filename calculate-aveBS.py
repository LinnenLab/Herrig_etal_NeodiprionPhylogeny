import re
from re import findall
import sys

bootstrapcutoff=sys.argv[1]

infile=open('keepforastral.matrix','r')
content=infile.read()
infile.close()
XMs=findall('XM_'+'[\S]+',content)


print('Calculating BSs and Filtering!')
outfile=open('bootstrapaves.txt','w')
treefile=open('filtered-parsANDsingleXMpergene-AND'+bootstrapcutoff+'minBSave.trees','w')
for XM in XMs:
    infile=open('20species_mRNA/'+XM+'.fa.treefile','r')
    content=infile.read()
    infile.close()
    bootstraps=findall('[0-9\.]+'+'/',content)
    bss=[]
    try:
        for bootstrap in bootstraps:
            bss.append(float(bootstrap.replace('/','')))
        avebootstrap=sum(bss)/len(bss)
        outfile.write(XM+'\t'+str(avebootstrap)+'\n')

    except:
        print('error with '+XM)
outfile.close()
treefile.close()
