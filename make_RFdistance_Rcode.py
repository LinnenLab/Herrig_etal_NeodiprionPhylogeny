numberoftrees=392

windowsize='500'

outfile=open('/Users/danielle/Desktop/phylogeny_maptoNlecref/2021_Nov/windows/painting/'+windowsize+'kb-distance.R','w')
outfile.write('library(ape)\n')
outfile.write('library(phangorn)\n')
outfile.write('library(phytools)\n')


outfile.write("speciestree <- read.tree('/Users/danielle/Desktop/phylogeny_maptoNlecref/2021_Nov/windows/1mb-astral.tre')\n")

outfile.write("windowtrees <- read.tree('/Users/danielle/Desktop/phylogeny_maptoNlecref/2021_Nov/windows/painting"+windowsize+"kb-filteredinfo.trees')\n")
outfile.write("speciestree\n")
outfile.write("windowtrees\n")
outfile.write('sink("/Users/danielle/Desktop/phylogeny_maptoNlecref/2021_Nov/windows/painting/'+windowsize+'kb-treedistance.matrix",append=TRUE)\n')

num=1
while num <= numberoftrees:
    outfile.write("cat(treedist(speciestree,windowtrees[["+str(num)+"]]),'\n')\n")
    num=num+1

outfile.write('sink()\n')
outfile.close()




