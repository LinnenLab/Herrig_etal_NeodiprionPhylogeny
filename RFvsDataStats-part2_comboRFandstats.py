import re
from re import findall
import sys

basedir='/Users/danielle/Desktop/phylogeny_maptoNlecref/2021_Nov/windows/'
size='50'

datastats={}
infile=open(basedir+size+'kbregion-datainfo.matrix','r')
for line in infile:
    info=line.split('\t')
    datastats[info[0]]=info[1]+'\t'+info[2]+'\t'+info[3]+'\t'+info[4]
infile.close()
print(len(datastats.keys()))

outfile=open(basedir+'speciesRF-'+size+'kbregion-datainfo.matrix','w')
outfile.write('region'+'\t'+'chromosome'+'\t'+'start'+'\t'+'stop'+'\t'+'tree'+'\t'+'RFdist'+'\t'+str('ambig')+'\t'+str('parsinfo')+'\t'+str('length')+'\t'+str('avebootstrap')+'\n')
infile=open(basedir+'painting/'+size+'kb-allinfo_withtreedist.txt','r')
for line in infile:
    if 'NA' not in line:
        info=line.split('\t')
        region='Chromosome'+info[0]+':'+info[1]+'-'+info[2]
        try:
            outfile.write(region+'\t'+info[0]+'\t'+info[1]+'\t'+info[2]+'\t'+info[3]+'\t'+info[5]+'\t'+datastats[region]+'\n')
        except:
            print('error with region '+region)
infile.close()
outfile.close()
print('DONE')
                  
