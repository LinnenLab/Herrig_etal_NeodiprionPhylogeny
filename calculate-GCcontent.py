import sys
import os
import re
from re import findall
from glob import glob

windowsize=int(sys.argv[1])

basedir='/scratch/dkhe223/pacbiorepit/windows_'+str(windowsize)+'kb/'
logdir=basedir+'20species_window'+str(windowsize)+'000/'
logfiles = glob(os.path.join(logdir,'*log'))


outfile=open(basedir+'GCcontent.matrix','w')
outfile.write('name'+'\t'+'C'+'\t'+'G'+'\t'+'CG'+'\n')
for logfile in logfiles:
    name=logfile.replace(logdir,'')
    name=name.replace('.fa.log','')
    
    try:
        infile=open(logfile,'r')
        content=infile.read()
        infile.close()

        Freqlines=findall('Base frequencies:  '+'[^\n]+',content)
        freqs=findall('0.'+'[0-9]+',Freqlines[0])

        outfile.write(name+'\t'+freqs[1]+'\t'+freqs[2]+'\t'+str(float(freqs[1])+float(freqs[2]))+'\n')
    except:		
        outfile.write(name+'\t'+'NA'+'\t'+'NA'+'\t'+'NA'+'NA'+'\n')
    

outfile.close()
