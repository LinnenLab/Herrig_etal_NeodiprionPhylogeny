import re
from re import findall
import sys

windowsize=sys.argv[1]
cutoff=0.1


keeplist=[]
allwindows=[]
aveinfo={}
infile=open('20sp_missing_'+windowsize+'kb.matrix','r')
for line in infile:
    if '>' not in line:
        tabs=findall('[^\t]+',line)
        allwindows.append(tabs[0])
        
        numslist=tabs[1:]
        nums=[]
        for num in numslist:
            nums.append(float(num))
        average=float(sum(nums))/float(len(nums))
        aveinfo[tabs[0]]=str(average)
        if average < cutoff:
            keeplist.append(tabs[0])
infile.close()

outfile=open('filteredmissing-20sp.trees','w')
outfileinfo=open('filteredinfo-20sp.matrix','w')
alltrees=open('alltrees.trees','w')
allinfo=open('allinfo.matrix','w')

scaffold=["notstarted"]
for window in allwindows:
##    if scaffold[0] not in window:
##        scaffold=findall('scaffold_'+'[0-9]+',window)
##        chrom=scaffold[0].replace('scaffold_','chr')
##        print(chrom)
##        num=1
    try:
        infile=open('20species_window'+windowsize+'000/'+window+'.fa.treefile','r')
        content=infile.read()
        infile.close()
        content=content.replace('\n','')
        if window in keeplist:
            outfile.write(content+'\n')
            outfileinfo.write(window+'\t'+content+'\n')
        alltrees.write(window+'\t'+content+'\n')
        allinfo.write(window+'\t'+content+'\t'+aveinfo[window]+'\n')
        
    except:
        alltrees.write(window+'\t'+'NA'+'\n')
        allinfo.write(window+'\t'+'NA'+'\t'+aveinfo[window]+'\n')
    #num=num+1

outfile.close()
outfileinfo.close()
alltrees.close()
