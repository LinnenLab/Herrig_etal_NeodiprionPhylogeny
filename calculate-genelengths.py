import sys
import os
import re
from re import findall
from glob import glob

basedir='/scratch/dkhe223/pacbiorepit/genes/'
logdir=basedir+'20species_mRNA/'
logfiles = glob(os.path.join(logdir,'*log'))


outfile=open(basedir+'genelength.matrix','w')
outfile.write('name'+'\t'+'pis'+'\t'+'singleton'+'\t'+'constant'+'\t'+'length'+'\n')
for logfile in logfiles:
    name=logfile.replace(logdir,'')
    name=name.replace('.fa.log','')

    infile=open(logfile,'r')
    content=infile.read()
    infile.close()

    sitelines=findall('[0-9]+'+' parsimony-informative, '+'[0-9]+'+' singleton sites, '+'[0-9]+'+' constant sites',content)
    nums=findall('[0-9]+',sitelines[0])

    outfile.write(name+'\t'+nums[0]+'\t'+nums[1]+'\t'+nums[2]+'\t'+str(int(nums[0])+int(nums[1])+int(nums[2]))+'\n')

outfile.close()
