speciestree <- read.tree('/Users/danielle/Desktop/phylogeny_maptoNlecref/TreesToTest/speciestree_binary.txt')
windowtrees <- read.tree('/Users/danielle/Desktop/phylogeny_maptoNlecref/original/IUPAC/windows_1mb/1mbgenome_treefile_noNA.txt')
tree1<-RF.dist(speciestree,windowtrees[[1]])

