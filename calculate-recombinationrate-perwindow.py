import sys
import re
from re import findall
from collections import Counter
import statistics

#windowsize=int(sys.argv[1]+'000')
windowsize=500000
inputkb='50'

currentchr='not started'
regionmax=int(windowsize)
currentrecomlist=[]
infosizelist=[]
listofone=0

infile=open('../ColorQTL_map_may2022-'+inputkb+'kb.csv','r')
outfile=open('../'+inputkb+'kb-'+str(windowsize)+'-recombinationrate.matrix','w')
outfile.write('region'+'\t'+'ave_recombinationrate'+'\t'+'min_recomrate'+'\t'+'max_recomrate'+'\n')
for line in infile:
    tabs=findall('[^,]+',line)
    #try:
    if 'Start' not in line:
        if tabs[0]==currentchr:
            if int(tabs[2]) <= regionmax:
                currentrecomlist.append(float(tabs[8]))
            elif len(currentrecomlist) > 0:
                outfile.write(currentchr+':'+str(regionmax-windowsize)+'-'+str(regionmax)+'\t'+str(sum(currentrecomlist)/float(len(currentrecomlist)))+'\t'+str(min(currentrecomlist))+'\t'+str(max(currentrecomlist))+'\n')
##                if currentchr == 'Chromosome1':
##                    print(currentchr,regionmax)
##                    print(currentrecomlist)
                
                if len(currentrecomlist) == 1:
                    listofone += 1
                else:
                    infosizelist.append(len(currentrecomlist))
                currentrecomlist=[]
                currentrecomlist.append(float(tabs[8]))
                regionmax=regionmax+windowsize
                #print(regionmax)
        else:
            try:
                outfile.write(currentchr+':'+str(regionmax-windowsize)+'-'+str(regionmax)+'\t'+str(sum(currentrecomlist)/float(len(currentrecomlist)))+'\t'+str(min(currentrecomlist))+'\t'+str(max(currentrecomlist))+'\n')
                print(currentchr,regionmax)
                print(currentrecomlist)
                
                if len(currentrecomlist) == 1:
                    listofone += 1
                else:
                    infosizelist.append(len(currentrecomlist))
                currentrecomlist=[]
                currentrecomlist.append(float(tabs[8]))
                regionmax=windowsize
                currentchr=tabs[0]
                #print(currentchr)
                
            except:
                while int(tabs[2]) > regionmax:
                    regionmax=regionmax+windowsize                   
                currentrecomlist.append(float(tabs[8]))
                print('except',line,regionmax)
                currentchr=tabs[0]
    #except:
        #print(line)

outfile.write(currentchr+':'+str(regionmax-windowsize)+'-'+str(regionmax)+'\t'+str(sum(currentrecomlist)/float(len(currentrecomlist)))+'\t'+str(min(currentrecomlist))+'\t'+str(max(currentrecomlist))+'\n')
print(currentchr,regionmax)
print(currentrecomlist)
infosizelist.append(len(currentrecomlist))
if len(currentrecomlist) == 1:
    listofone += 1
infile.close()
outfile.close()

print(min(infosizelist))
print(float(sum(infosizelist))/float(len(infosizelist)))
print(max(infosizelist))

print(statistics.mode(infosizelist))

print(listofone)
            
            
            
            
        
