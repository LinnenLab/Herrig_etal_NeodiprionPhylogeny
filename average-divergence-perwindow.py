import re
from re import findall
import os

Chrom='Chromosome1'

infile=open('regions.txt','r')
content=infile.read()
infile.close()
regions=findall('[^\n]+',content)

specieslist=['aut','lec','abb','com','dub','exc','fab','het','kne','mau','mer','nig','pine','piri','pra','rug','swa','tae','vir','war']
firstnum=0
topline='region'+'\t'+'average'
while firstnum < len(specieslist):
    complist=specieslist[firstnum+1:]
    #print(specieslist[firstnum])
    #print(complist)
    for species in complist:
        topline += '\t'+specieslist[firstnum]+'-'+species
    firstnum=firstnum+1   
print(topline)
outfile=open(Chrom+'-average-k80dist.dna.matrix','w')
outfile.write(topline+'\n')

for region in regions:
    if Chrom in region:
        try:
            region=region.replace(':','_')
            infile=open('distance-'+region+'.csv','r')
            distances=[]
            starttab=2
            header='yes'
            for line in infile:
                if header == 'yes':
                    header='no'
                elif 'warreni' not in line:
                    info=findall('[^,]+',line)
                    distances=distances+info[starttab:]
                    starttab=starttab+1
            floatdistances=[]
            pairwise=''
            for distance in distances:
                distance=distance.replace('\n','')
                floatdistances.append(float(distance))
                pairwise += '\t'+distance
        except:
            print(region)

outfile.close()
        
        
