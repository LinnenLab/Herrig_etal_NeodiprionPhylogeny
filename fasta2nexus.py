import sys
import re
from re import findall

windowsize=sys.argv[1]

chrnum=1
fastasdict={}
while chrnum<8:
    print('starting chromosome '+str(chrnum))
    infile=open(windowsize+'_chr'+str(chrnum)+'.fasta','r')
    for line in infile:
        line=line.replace('\n','')
        if '>' in line:
            species=line.replace('>','')
        else:
            try:
                temp=fastasdict[species]
                temp=temp+line
                fastasdict[species]=temp
                if species == 'Nlec_HiC_scaffolds_primary':
                    counter=counter+len(line)
                    print(counter)
            except:
                fastasdict[species]=line
                counter=len(line)
                print(species, counter)
    chrnum=chrnum+1

specieslist=list(fastasdict.keys())
specieslist.sort()
print(counter)


outfile=open(windowsize+'kb_genome.nex','w')
towritebase='#NEXUS\n\nBEGIN DATA;\nDIMENSIONS NTAX=20 NCHAR='+str(counter)+';\nFORMAT DATATYPE=DNA MISSING=N GAP=- ;\nMATRIX\n'
outfile.write(towritebase)
for species in specieslist:
    outfile.write(species+' '+fastasdict[species]+'\n')
outfile.write(';\nEND;\n')
outfile.close()