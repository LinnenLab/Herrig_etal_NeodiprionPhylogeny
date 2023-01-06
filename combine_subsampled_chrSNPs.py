import sys
import re
from re import findall

Basename=sys.argv[1]

chrnum=1

genomedict={}
specieslist=[]
infile=open('species.txt')
for line in infile:
    genomedict[line]=line
    specieslist.append(line)

while chrnum < 8:
    infile=open(Basename+'kb_chr'+str(chrnum)+'.fasta')
    currentseq=''
    for line in infile:
        if '>' in line:
            #print(line)
            try:
                seq=genomedict[currentspecies]+currentseq
                genomedict[currentspecies]=seq
            except:
                print('just starting')
            currentseq=''
            currentspecies=line
        else:
            temp=line.replace('\n','')
            currentseq=currentseq+temp
    seq=genomedict[currentspecies]+currentseq
    genomedict[currentspecies]=seq
    infile.close()
    chrnum = chrnum + 1

outfile=open(Basename+'kb_genome.fasta','w')

for species in specieslist:
    print(species)
    outfile.write(genomedict[species]+'\n')
outfile.close()
        
    
