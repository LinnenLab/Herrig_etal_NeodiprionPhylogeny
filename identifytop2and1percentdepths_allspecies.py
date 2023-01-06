import re
from re import findall

tabre='[^\t]+'

directory=''
specieslanedict={'abbotii':'001-04','abietis':'360-02-1','autumnalis':'060-03','compar':'089-04','dubiosus':'221-04','excitans':'033-04','fabricii':'006-04','hetricki':'057-04','knereri':'081-04a','leconteiN':'168-02','leconteiS':'RB130','maurus':'NMr003-1-1','merkeli':'184-03-1','nigroscutum':'209-04','pinetum':'377-02','pinusrigidae':'142-04','pratti':'054-04','rugifrons':'184-02c','sertifer':'Ns032A-3a','swainei':'257-02b','taedae':'002-04a2','virginianus':'126-04-1','warreni':'093-04'}
#specieslanedict={'abbotii':'001-04'}
                 
specieslist=specieslanedict.keys()
specieslist.sort()

scaffold='not started'

outfile=open('top2and1percentcutoffs_allspecies.matrix','w')
outfile.write('species'+'\t'+'2%cutoffnumber'+'\t'+'1%cutoffnumber'+'\t'+'totalnucleotides'+'\n')


speciesdict={}
for species in specieslist:
    try:
        infilename=species+'/'+species+'_final.depth.matrix'
        infile=open(infilename)
        print(infilename)

        totalcount=0
        topdepthlist=[]
        
        for line in infile:
            try:
                if 'Chromosome' in line:
                    totalcount=totalcount+1
                    tabs=findall(tabre,line)
                    if int(tabs[2]) > 20:
                        topdepthlist.append(int(tabs[2]))
            except:
                print(line)
        infile.close()
        print(totalcount)
        percent2=0.02*totalcount
        percent1=0.01*totalcount
        topdepthlist.sort()
        print(topdepthlist[-10:])
        cutoff2=str(topdepthlist[-int(percent2)])
        cutoff1=str(topdepthlist[-int(percent1)])
        outfile.write(species+'\t'+cutoff2+'\t'+cutoff1+'\t'+str(totalcount)+'\n')

    except:
        print('ERROR with '+species)

    
                
outfile.close()
