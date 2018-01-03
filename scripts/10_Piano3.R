source("https://bioconductor.org/biocLite.R")
library('piano')
library(gplots)

HS_dir <- "/Users/xueqingwang/Documents/semester3/Analysis of Data from High-Throughput Molecular Biology Experiments/Project/Results_My/atlas_all_HS_DESeq2.tsv"
HS<-read.table(HS_dir,sep='\t',header = TRUE)
HS<-HS[complete.cases(HS),]
HS<-HS[!duplicated(HS$Gene),]
HS<-data.frame(HS)

fc<-HS$log2FoldChange
pv<-HS$P_value
names(fc)=HS$Gene
names(pv)=HS$Gene

kegg <- loadGSC("/Users/xueqingwang/Documents/semester3/Analysis of Data from High-Throughput Molecular Biology Experiments/Project/Library/c2.cp.kegg.v6.1.symbols.gmt")
go <- loadGSC("/Users/xueqingwang/Documents/semester3/Analysis of Data from High-Throughput Molecular Biology Experiments/Project/Library/c5.bp.v6.1.symbols.gmt")
onco <- loadGSC("/Users/xueqingwang/Documents/semester3/Analysis of Data from High-Throughput Molecular Biology Experiments/Project/Library/c6.all.v6.1.symbols.gmt")

gsaRes_HS_kegg <- runGSA(pv, fc, gsc=kegg, geneSetStat="reporter", 
                         signifMethod="nullDist", nPerm=1000, verbose=TRUE)


GSAsummaryTable(gsaRes_HS_kegg, save=TRUE, file="/Users/xueqingwang/Documents/semester3/Analysis of Data from High-Throughput Molecular Biology Experiments/Project/Results_My/HSnodu4_0102_kegg_DESeq2_piano.xls")
par(mar = c(1,3,4,1.5))##bottom,left,top,right
#nw <- networkPlot(gsaRes_HS_kegg,class="non", label = "numbers")
nw <- networkPlot(gsaRes_HS_go, class="distinct", direction="both",
                  significance=0.0005, label="numbers")
gsaRes_HS_go <- runGSA(pv,fc,gsc=go, geneSetStat="reporter", 
                           signifMethod="nullDist", nPerm=1000, verbose=TRUE)

#nw <- networkPlot(gsaRes_HS_go,class="non", 
                  #significance = 0.0005, label = "numbers")
#nw$geneSets[1:400]
#image(as.matrix(nw),col=cx,axes=T)
GSAsummaryTable(gsaRes_HS_go, save=TRUE, file="/Users/xueqingwang/Documents/semester3/Analysis of Data from High-Throughput Molecular Biology Experiments/Project/Results_My/HSnodu4_0102_go_DESeq2_piano.xls")
#gsaRes_HS_onco <- runGSA(pv, fc, gsc=onco, geneSetStat="reporter", 
#                          signifMethod="nullDist", nPerm=1000, verbose=TRUE)
#GSAsummaryTable(gsaRes_HS_onco, save=TRUE, file="/Users/xueqingwang/Documents/semester3/Analysis of Data from High-Throughput Molecular Biology Experiments/Project/Results_My/HSnodu2_onco_DESeq2_piano.xls")nw