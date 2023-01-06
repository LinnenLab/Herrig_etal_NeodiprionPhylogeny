import re
from re import findall
import sys

size=sys.argv[1]

infile=open('filteredinfo-20sp.matrix','r')
content=infile.read()
infile.close()

regions=findall('Chromosome'+'[\S]+',content)
print(len(regions))
print(regions[0])

outfile=open(size+'kbregion-datainfo-filteredonly.matrix','w')
outfile.write('region'+'\t'+str('ambig')+'\t'+str('parsinfo')+'\t'+str('length')+'\t'+str('avebootstrap')+'\n')
for region in regions:
    try:
        infile=open('20species_window'+size+'000/'+region+'.fa.log','r')
        content=infile.read()
        infile.close()
        length=findall('[0-9]+'+' columns',content)
        parsinfo=findall('[0-9]+'+' parsimony-informative',content)
        ambig=findall('TOTAL'+'[^%]+',content)
        ambig=findall('[0-9]+'+'.'+'[0-9]+',ambig[0])

        length=int(length[0].replace(' columns',''))
        parsinfo=int(parsinfo[0].replace(' parsimony-informative',''))
        ambig=float(ambig[0])

        infile=open('20species_window'+size+'000/'+region+'.fa.treefile','r')
        content=infile.read()
        infile.close()
        bootstraps=findall('[0-9\.]+'+'/',content)
        bss=[]
        for bootstrap in bootstraps:
            bss.append(float(bootstrap.replace('/','')))
        avebootstrap=sum(bss)/len(bss)
        outfile.write(region+'\t'+str(ambig)+'\t'+str(parsinfo)+'\t'+str(length)+'\t'+str(avebootstrap)+'\n')
    except:
        print('there was an error with '+region)
outfile.close()


                    

    
    
    
