import re
from re import findall
import sys

infile=open('mRNA.txt','r')
groupnumber=0
submitcommand="echo submitting"+'\n'

currentcount=0
iqcommands=''

for line in infile:
    name=line.replace('\n','')
    iqcommands=iqcommands+'iqtree -s ../internal_mRNA/'+name+'.fa -o autumnalis -m MFP -bb 1000 -alrt 1000'+'\n'
    currentcount=currentcount+1
    
    if currentcount == 1000:
        outfilename='iqtrees_'+str(groupnumber)+'.job'
        outfile=open('internal_iqtreejobs/'+outfilename,'w')
        towrite='#!/bin/bash'+'\n'+'#SBATCH -t 7-00:00:00'+'\n'+'#SBATCH --job-name=int_'+str(groupnumber)+'\n'
        towrite=towrite+'\n'+'#SBATCH -n 1'+'\n'+'#SBATCH -p HAS24M128_M'+'\n'+'#SBATCH --account=col_cli242_uksr'+'\n'+'#SBATCH --mail-type ALL'+'\n'+'#SBATCH --mail-user dkhe223@uky.edu'+'\n'
        towrite=towrite+'#SBATCH --output=int'+str(groupnumber)+'.out'+'\n'
        towrite=towrite+'\n'+'module load ccs/anaconda/3'+'\n'+'source activate /project/cli242_uksr/dkhe223/conda/phylogenies'+'\n'+'\n'
        towrite=towrite+'\n'
        towrite=towrite+'\n'+iqcommands
        outfile.write(towrite)
        outfile.close()

        submitcommand=submitcommand+'sbatch '+outfilename+'\n'
        
        currentcount=0
        groupnumber=groupnumber+1
        iqcommands=''
    
outfilename='int_'+str(groupnumber)+'.job'
submitcommand=submitcommand+'sbatch '+outfilename+'\n'
outfile=open('internal_iqtreejobs/'+outfilename,'w')
towrite='#!/bin/bash'+'\n'+'#SBATCH -t 7-00:00:00'+'\n'+'#SBATCH --job-name=int_'+str(groupnumber)+'\n'
towrite=towrite+'\n'+'#SBATCH -n 1'+'\n'+'#SBATCH -p HAS24M128_M'+'\n'+'#SBATCH --account=col_cli242_uksr'+'\n'+'#SBATCH --mail-type ALL'+'\n'+'#SBATCH --mail-user dkhe223@uky.edu'+'\n'
towrite=towrite+'#SBATCH --output=int'+str(groupnumber)+'.out'+'\n'
towrite=towrite+'\n'+'module load ccs/anaconda/3'+'\n'+'source activate /project/cli242_uksr/dkhe223/conda/phylogenies'+'\n'+'\n'
towrite=towrite+name+'\n'
towrite=towrite+'\n'+iqcommands
outfile.write(towrite)
outfile.close()          
infile.close()

outfile=open('internal_iqtreejobs/'+'submitiqtrees','w')
outfile.write(submitcommand)
outfile.close()
