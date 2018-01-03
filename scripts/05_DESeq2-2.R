directory <- "../DATA/mapping2.tsv"
data <- read.table(directory, sep='\t', header=TRUE, row.names=1)
N <- nrow(data)

healthy <- data[,grepl("H",names(data))]
steatosis <- data[,grepl("S",names(data))]
nash <- data[,grepl("N",names(data))]
cancer <- data[,grepl("C",names(data))]

source("http://www.bioconductor.org/biocLite.R")
library("DESeq2")

total_data <- cbind(healthy, steatosis, nash, cancer)
total_data <- round(total_data,0)
col_names <- colnames(total_data)
condition <- c(rep("H", length(healthy)), rep("S", length(steatosis)), rep("N", length(nash)), rep("C", length(cancer)))
(coldata <- data.frame(row.names=colnames(total_data), condition))

dds <- DESeqDataSetFromMatrix(countData=total_data, colData=coldata, design=~condition)
dds <- DESeq(dds)

HS <- data.frame(results(dds, contrast = c('condition', "H", "S")))
SN <- data.frame(results(dds, contrast = c('condition', "S", "N")))
NC <- data.frame(results(dds, contrast = c('condition', "N", "C")))

write.table(HS, file="../Results_My/HS_Seq2.tsv", sep='\t')
write.table(SN, file="../Results_My/SN_Seq2.tsv", sep='\t')
write.table(NC, file="../Results_My/NC_Seq2.tsv", sep='\t')