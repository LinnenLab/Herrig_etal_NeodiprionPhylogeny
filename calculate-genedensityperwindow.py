import sys
import re
from re import findall

windowsize=int(sys.argv[1]+'000')

infile=open('regions.txt','r')
content=infile.read()
infile.close()
regions=findall('[\S]+',content)

regiondict={}
currentchr='Chromosome1'
regionmax=int(windowsize)
currentgenecount=0

infile=open('../data/iyNeoLeco1.1_genomic-genesonly.gff','r')
outfile=open(str(windowsize)+'-genedensities.matrix','w')
outfile.write('region'+'\t'+'genecount'+'\n')
for line in infile:
    tabs=findall('[\S]+',line)
    if tabs[0]==currentchr:
        if int(tabs[3]) < regionmax:
            currentgenecount += 1
        else:
            print(currentchr+':'+str(regionmax-int(windowsize))+'-'+str(regionmax)+'\t'+str(currentgenecount))
            outfile.write(currentchr+':'+str(regionmax-int(windowsize))+'-'+str(regionmax)+'\t'+str(currentgenecount)+'\n')
            currentgenecount=1
            regionmax=regionmax+windowsize
    else:
        outfile.write(currentchr+':'+str(regionmax-windowsize)+'-'+str(regionmax)+'\t'+str(currentgenecount)+'\n')
        currentgenecount=1
        regionmax=windowsize
        currentchr=tabs[0]
infile.close()
outfile.close()
        
            
            
            
            
        
