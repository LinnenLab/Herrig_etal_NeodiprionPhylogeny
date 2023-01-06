import re
from re import findall

tabre='[^\t]+'

directory=''
specieslanedict={'abbotii':'001-04','abietis':'360-02-1','autumnalis':'060-03','compar':'089-04','dubiosus':'221-04','excitans':'033-04','fabricii':'006-04','hetricki':'057-04','knereri':'081-04a','leconteiN':'168-02','leconteiS':'RB130','maurus':'NMr003-1-1','merkeli':'184-03-1','nigroscutum':'209-04','pinetum':'377-02','pinusrigidae':'142-04','pratti':'054-04','rugifrons':'184-02c','sertifer':'Ns032A-3a','swainei':'257-02b','taedae':'002-04a2','virginianus':'126-04-1','warreni':'093-04'}
#specieslanedict={'abbotii':'001-04'}
                 
specieslist=list(specieslanedict.keys())
specieslist.sort()

depthlimits={}
infile=open('../top2and1percentcutoffs_allspecies.matrix')
for line in infile:
    try:
        tabs=findall(tabre,line)
        depthlimits[tabs[0]]=int(tabs[2])
    except:
        print(line)
infile.close()


mindepth=4
maxdepth=depthlimits['currentspecies']
print(maxdepth)
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
fasta=open(outfilebase+'_rd'+str(mindepth)+'to'+'top1percent'+'orN.fa', 'w')
newNcount=0
totalnuc=0
currentchr='notstarted'

for line in infile:
    if '>' in line:
        if currentchr != 'notstarted':
            fasta.write(fastaline+'\n')
            print(currentchr+'has '+str(position-1)+' nucleodites')
            if 'Chromosome' in line:
                totalnuc=totalnuc+position-1
        currentchr=line
        currentchr=currentchr.replace('>','')
        currentchr=currentchr.replace('\n','')
        print(currentchr)
        position=1
        fastacount=0
        fastaline=''
        fasta.write(line)
        
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
                if 'Chromosome' in currentchr:
                    newNcount=newNcount+1
            
fasta.write(fastaline+'\n')
print(currentchr+'has '+str(position-1)+' nucleodites')
print('There are '+str(newNcount)+'Ns inserted due to read depths less than '+str(mindepth)+' or more than '+str(maxdepth)+' out of '+str(totalnuc)+' nucleotides in the first 7 scaffolds')
infile.close()
matrix.close()
fasta.close()
