import re
from re import findall

windowsize='500'
directory='/Users/danielle/Desktop/phylogeny_maptoNlecref/2021_Nov/windows/painting/'

####COMBINE filtered info name with tree distances
filtereddict={}
infile=open(directory+windowsize+'kb-filteredinfo.matrix','r')
content=infile.read()
infile.close()
filteredlines=findall('[^\n]+',content)
print(len(filteredlines))

infile=open(directory+windowsize+'kb-treedistance.matrix','r')
content=infile.read()
infile.close()
treedistance=findall('[^\n]+',content)
print(len(treedistance))

counter=0
#since they are the same length and order, we can iterate through them at the same time to assign names to tree distances
while counter < len(filteredlines):
    info=findall('[\S]+',filteredlines[counter])
    name=info[0]
    treedist=treedistance[counter].replace(' ',',')
    filtereddict[name]=treedist
    counter+=1
print(filtereddict[name])



####COMBINE filtered info/treedistances with all info
infile=open(directory+windowsize+'kb-allinfo.matrix','r')
outfile=open(directory+windowsize+'kb-allinfo_withtreedist.csv','w')
for line in infile:
    tabs=findall('[\S]+',line)
    name=tabs[0]
    info=tabs[0]+','+'"'+tabs[1]+'",'+tabs[2]
    try:
        outfile.write(info+','+filtereddict[name]+'\n')
    except:
        outfile.write(info+','+'NA,NA,NA,NA,'+'\n')
infile.close()
outfile.close()


####COMBINE filtered info/treedistances with all info AND replace names to locations
infile=open(directory+windowsize+'kb-allinfo.matrix','r')
outfile=open(directory+windowsize+'kb-allinfo_withtreedist.csv','w')
for line in infile:
    tabs=findall('[\S]+',line)
    name=tabs[0]
    locationinfo=findall('[^:^-]+',tabs[0])
    #info=locationinfo[0]
    info=locationinfo[0].replace('Chromosome','')

    #add treedistance info
    if info != 'notstarted':
        info=info+','+locationinfo[1]+','+locationinfo[2]+','+'"'+tabs[1]+'",'+tabs[2]
        try:
            outfile.write(info+','+filtereddict[name]+'\n')
        except:
            outfile.write(info+','+'NA,NA,NA,NA,'+'\n')
        
infile.close()
outfile.close()

        
        


    
        
