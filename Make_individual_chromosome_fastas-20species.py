import re
from re import findall
from glob import glob
import sys
import os

basedir=sys.argv[1]

tabre='[^\t]+'
windowre='PGA_'+'[\S]+'

chrom1=open(basedir+'chromosomes/chr1.fa','w')
chrom2=open(basedir+'chromosomes/chr2.fa','w')
chrom3=open(basedir+'chromosomes/chr3.fa','w')
chrom4=open(basedir+'chromosomes/chr4.fa','w')
chrom5=open(basedir+'chromosomes/chr5.fa','w')
chrom6=open(basedir+'chromosomes/chr6.fa','w')
chrom7=open(basedir+'chromosomes/chr7.fa','w')

#genomelist=['lecontei_pacbio','abbotii','autumnalis','compar','dubiosus','excitans','fabricii','hetricki','knereri','leconteiN','leconteiS','maurus','merkeli','nigroscutum','pinetum','pinusrigidae','pratti','rugifrons','swainei','taedae','virginianus','warreni']
genomelist = glob(os.path.join(basedir+'wholefasta/','*fa'))
for genome in genomelist:
    infile=open(genome,'r')
    genome=genome.replace(basedir+'wholefasta/','')
    print(genome)
    currentchr='notstarted'
    for line in infile:
        if '>' in line:
            add='no'
            nums=findall('[0-9]+',line)
            currentchr='chr'+nums[0]
            if currentchr== 'chr1':
                chrom1.write('>'+genome+'\n')
            elif currentchr == 'chr2':
                chrom2.write('>'+genome+'\n')
            elif currentchr== 'chr3':
                chrom3.write('>'+genome+'\n')
            elif currentchr == 'chr4':
                chrom4.write('>'+genome+'\n')
            elif currentchr == 'chr5':
                chrom5.write('>'+genome+'\n')
            elif currentchr == 'chr6':
                chrom6.write('>'+genome+'\n')
            elif currentchr == 'chr7':
                chrom7.write('>'+genome+'\n')
        else:
            if currentchr == 'chr1':
                chrom1.write(line)
            elif currentchr == 'chr2':
                chrom2.write(line)
            elif currentchr == 'chr3':
                chrom3.write(line)
            elif currentchr == 'chr4':
                chrom4.write(line)
            elif currentchr == 'chr5':
                chrom5.write(line)
            elif currentchr == 'chr6':
                chrom6.write(line)
            elif currentchr == 'chr7':
                chrom7.write(line)
    infile.close()

chrom1.close()
chrom2.close()
chrom3.close()
chrom4.close()
chrom5.close()
chrom6.close()
chrom7.close()
