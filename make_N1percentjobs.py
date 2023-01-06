specieslanedict={'abbotii':'001-04','abietis':'360-02-1','autumnalis':'060-03','compar':'089-04','dubiosus':'221-04','excitans':'033-04','fabricii':'006-04','hetricki':'057-04','knereri':'081-04a','leconteiN':'168-02','leconteiS':'RB130','maurus':'NMr003-1-1','merkeli':'184-03-1','nigroscutum':'209-04','pinetum':'377-02','pinusrigidae':'142-04','pratti':'054-04','rugifrons':'184-02c','sertifer':'Ns032A-3a','swainei':'257-02b','taedae':'002-04a2','virginianus':'126-04-1','warreni':'093-04'} 

infile=open('base_N1percenttop.job') 
content=infile.read()
infile.close() 
specieslist=specieslanedict.keys()
submit=open('fordepthjobs/submitjobs.sh','w')
for species in specieslist:
    submit.write('sbatch '+species+'_N1percenttop.job'+'\n')
    outfilename='fordepthjobs/'+species+'_N1percenttop.job' 
    towrite=content 
    towrite=towrite.replace('speciesname',species) 
    towrite=towrite.replace('laneinfo',specieslanedict[species]) 
    outfile=open(outfilename, 'w') 
    outfile.write(towrite) 
    outfile.close()
submit.close()
