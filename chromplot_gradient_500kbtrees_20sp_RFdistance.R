if (!requireNamespace("BiocManager", quietly = TRUE))
install.packages("BiocManager")

BiocManager::install("chromPlot")
a
yes
library("chromPlot")

window_trees <- read.csv('/Users/danielle/Desktop/phylogeny_maptoNlecref/2021_Nov/windows/painting/500kb-allinfo_withtreedist.csv')
head(window_trees)
colnames(window_trees) <- c("Chrom", "Start", "End","tree","ave","RFdist","branch.score.diff","path.diff","weighted.path.diff")

library(RColorBrewer)
display.brewer.pal(9,"YlGnBu")
colors<-brewer.pal(9,"YlGnBu")
#colors

window_trees$Colors <- ifelse(window_trees$RFdist == "0", "mediumpurple",
                              ifelse(window_trees$RFdist == "2", colors[8],
                                     ifelse(window_trees$RFdist == "4", colors[7],
                                            ifelse(window_trees$RFdist == "6", colors[6],
                                                   ifelse(window_trees$RFdist == "8", colors[5],
                                                          ifelse(window_trees$RFdist == "10", colors[4],
                                                                 ifelse(window_trees$RFdist == "12", colors[3],
                                                                        ifelse(window_trees$RFdist == "14", colors[2], 
                                                                               ifelse(window_trees$RFdist == "16", colors[1],
                                                                                      ifelse(window_trees$RFdist == "18", "gold",
                                                                                             ifelse(window_trees$RFdist == "20", "gold",
                                                                                                    ifelse(window_trees$RFdist == "22", "gold",
                                                                                                           ifelse(window_trees$RFdist == "24", "gold",
                                                                                                                                                    ifelse(window_trees$RFdist == "34", colors[1],
                                                                                             ifelse(window_trees$RFdist == "NA", "grey","gold")))))))))))))))

head(window_trees)

pdf("/Users/danielle/Desktop/phylogeny_maptoNlecref/2021_Nov/windows/painting/500kb-RFtoastral.pdf")
painted <- chromPlot(bands=window_trees, figCols=100)
dev.off()
