import sys
import re
from re import findall

windowsize=int(sys.argv[1]+'000')

infile=open('regions.txt','r')
content=infile.read()
infile.close()
regions=findall('[\S]+',content)

prevchrom='Chromosome1'
regiondict={}
for region in regions:
    regiondict[region]=0
    if prevchrom not in region:
        print(prevregion)
        if "Chromosome1" in prevregion:
            endChr1=prevregion
        elif "Chromosome2" in prevregion:
            endChr2=prevregion
        elif "Chromosome3" in prevregion:
            endChr3=prevregion
        elif "Chromosome4" in prevregion:
            endChr4=prevregion
        elif "Chromosome5" in prevregion:
            endChr5=prevregion
        elif "Chromosome6" in prevregion:
            endChr6=prevregion
        prevchrom=findall('Chromosome'+'[0-9]',region)[0]
        
    prevregion=region
print(region)
endChr7=prevregion

infile=open('../data/iyNeoLeco1.1_genomic-genesonly.gff','r')
for line in infile:
    if 'Chromosome' in line:
        try:
            tabs=findall('[\S]+',line)
            start=int(tabs[3])
            #define region start--since start and windowsize are integers, it will round down and go to the region start
        ##    floatdiv=float(start)/float(windowsize)
        ##    div=start/windowsize
        ##    regionstart=div*windowsize
        ##    if div > floatdiv:
        ##        print(floatdiv,div,regionstart)
            regionstart=start/windowsize*windowsize
            region=tabs[0]+':'+str(regionstart)+'-'+str(regionstart+windowsize)
            regiondict[region] += 1
        except:
            if "Chromosome1" in tabs[0]:
                region=endChr1
            elif "Chromosome2" in tabs[0]:
                region=endChr2
            elif "Chromosome3" in tabs[0]:
                region=endChr3
            elif "Chromosome4" in tabs[0]:
                region=endChr4
            elif "Chromosome5" in tabs[0]:
                region=endChr5
            elif "Chromosome6" in tabs[0]:
                region=endChr6
            elif "Chromosome7" in tabs[0]:
                region=endChr7
            print(tabs[0],regionstart)
            regiondict[region] += 1
            #region=input('specify region')
infile.close()

outfile=open(str(windowsize)+'-genedensities.matrix','w')
outfile.write('region'+'\t'+'genecount'+'\n')
for region in regions:
    outfile.write(region+'\t'+str(regiondict[region])+'\n')
outfile.close()
        
            
            
            
            
        
