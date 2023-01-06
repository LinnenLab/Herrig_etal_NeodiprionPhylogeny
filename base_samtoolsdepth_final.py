mindepth=4 
maxdepth=40 

import re 
from re import findall 

linere='[^\n]+' 
tabre='[^\t]+' 
spacere='[\S]+' 

print("identify positions with required depth") 
depthdict={} 
chrset=set([]) 
infilename='currentspecies_final.depth.matrix' 

#infilename='chr1.depth.matrix' 
print(infilename) 
infile=open(infilename, 'r') 
for line in infile: 
    try: 
        tabs=findall(tabre,line) 
        depthdict[tabs[0]][tabs[1]]=tabs[2] 
        #print(depthdict) 
    except: 
        depthdict[tabs[0]]={} 
        depthdict[tabs[0]][tabs[1]]=tabs[2] 
        #print(line) 
print([tabs[0]],[tabs[1]],depthdict[tabs[0]][tabs[1]]) 
print(depthdict[tabs[0]]['1']) 
infile.close()

infilename='iupac_it5_currentspecies.fa' 
print(infilename) 
infile=open(infilename, 'r') 
outfilebase='currentspecies_iupac_it5.depth_withnucleotide' 
matrix=open(outfilebase+'.matrix', 'w') 
fasta=open(outfilebase+'_rd'+str(mindepth)+'to'+str(maxdepth)+'orN.fa', 'w') 
newNcount=0 
totalnuc=0 
currentchr='notstarted' 
scaff8='no' 

for line in infile: 
    if '>' in line: 
        if currentchr != 'notstarted': 
            fasta.write(fastaline+'\n') 
            print(currentchr+'has '+str(position-1)+' nucleodites') 
            if scaff8 == 'no': 
                totalnuc=totalnuc+position-1 
        currentchr=line 
        currentchr=currentchr.replace('>','') 
        currentchr=currentchr.replace('\n','') 
        print(currentchr) 
        position=1 
        fastacount=0 
        fastaline='' 
        fasta.write(line) 
        if 'scaffold_8_' in line: 
            scaff8='yes' 
         
    else: 
        nucleotides=findall('[\S]',line) 
        for nucleotide in nucleotides: 
            if fastacount == 60: 
                fasta.write(fastaline+'\n') 
                fastacount=0 
                fastaline='' 
            fastacount=fastacount+1 
            #note: the next try/except was put in to allow for linkage groups that had no reads mapping to them 
            try: 
                currentdepth=int(depthdict[currentchr][str(position)]) 
            except: 
                currentdepth=0 
            matrix.write(currentchr+'\t'+str(position)+'\t'+str(currentdepth)+'\t'+nucleotide+'\n') 
            position=position+1 
            if currentdepth >= mindepth and currentdepth <= maxdepth: 
                fastaline=fastaline+nucleotide 
            else: 
                fastaline=fastaline+'N' 
                if scaff8 == 'no': 
                    newNcount=newNcount+1 

fasta.write(fastaline+'\n') 
print(currentchr+'has '+str(position-1)+' nucleodites') 
print('There are '+str(newNcount)+'Ns inserted due to read depths less than '+str(mindepth)+' or more than '+str(maxdepth)+' out of '+str(totalnuc)+' nucleotides in the first 7 scaffolds') 
infile.close() 
matrix.close() 
fasta.close() 
