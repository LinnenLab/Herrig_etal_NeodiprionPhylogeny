import sys
import re
from re import findall

Basename=sys.argv[1]
InfoFile=open(Basename+'vcf.INFO','r')

Infodict={}
for line in InfoFile:
    tabs=findall('[\S]+',line)
    second=tabs[3].replace(',','')
    Infodict[tabs[1]]=list(tabs[2])+list(second)
#print(Infodict)

GenotypeFile=open(Basename+'vcf.GT.FORMAT','r')
for line in GenotypeFile:
    tabs=findall('[\S]+',line)
    if "CHROM" in line:
        tabs=findall('[\S]+',line)
        specieslist=tabs[2:]
        fastasdict={}
        for species in specieslist:
            fastasdict[species]='>'+species+'\n'
    else:
        counter=0
        genotypes=tabs[2:]
        for genotype in genotypes:
            nuc=Infodict[tabs[1]]#[int[genotype]]
            nuc=Infodict[tabs[1]][int(genotype)]
            #print(type(nuc),nuc)
            fasta=fastasdict[specieslist[counter]]+nuc
            fastasdict[specieslist[counter]]=fasta
            #print(fastasdict)
            counter=counter+1

print(fastasdict[specieslist[0]])
outfile=open(Basename+'.fasta','w')
for species in specieslist:
    outfile.write(fastasdict[species]+'\n')
outfile.close()
    





