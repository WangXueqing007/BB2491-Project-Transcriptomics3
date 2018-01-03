source("https://bioconductor.org/biocLite.R")
library('piano')
library(gplots)

#NC now...
HS_dir <- "/Users/xueqingwang/Documents/semester3/Analysis of Data from High-Throughput Molecular Biology Experiments/Project/Results_My/atlas_all_NC_DESeq2.tsv"
HS<-read.table(HS_dir,sep='\t',header = TRUE)
HS<-HS[complete.cases(HS),]
HS<-HS[!duplicated(HS$Gene),]
HS<-data.frame(HS)

fc<-HS$log2FoldChange
pv<-HS$P_value
names(fc)=HS$Gene
names(pv)=HS$Gene

kegg <- loadGSC("/Users/xueqingwang/Documents/semester3/Analysis of Data from High-Throughput Molecular Biology Experiments/Project/Library/c2.cp.kegg.v6.1.symbols.gmt")
#go <- loadGSC("/Users/xueqingwang/Documents/semester3/Analysis of Data from High-Throughput Molecular Biology Experiments/Project/Library/c5.bp.v6.1.symbols.gmt")
#onco <- loadGSC("/Users/xueqingwang/Documents/semester3/Analysis of Data from High-Throughput Molecular Biology Experiments/Project/Library/c6.all.v6.1.symbols.gmt")

gsaRes_HS_kegg1_1 <- runGSA(pv, fc, gsc=kegg, geneSetStat="reporter", 
                 signifMethod="nullDist", nPerm=1000, verbose=TRUE)
GSAsummaryTable(gsaRes_HS_kegg1_1, save=TRUE, file="/Users/xueqingwang/Documents/semester3/Analysis of Data from High-Throughput Molecular Biology Experiments/Project/Results_My/HeatMap/NC0102reporter_kegg_DESeq2_piano.xls")

gsaRes_HS_kegg1_2 <- runGSA(pv, fc, gsc=kegg, geneSetStat="reporter", 
                             nPerm=1000, verbose=TRUE)
GSAsummaryTable(gsaRes_HS_kegg1_2, save=TRUE, file="/Users/xueqingwang/Documents/semester3/Analysis of Data from High-Throughput Molecular Biology Experiments/Project/Results_My/HeatMap/NC0102reporter_kegg_DESeq2_piano.xls")


#gsaRes_HS_kegg2_1 <- runGSA(pv, fc, gsc=kegg, geneSetStat="tailStrength", 
                          #signifMethod="nullDist", nPerm=1000, verbose=TRUE)
#GSAsummaryTable(gsaRes_HS_kegg2_1, save=TRUE, 
                #file="/Users/xueqingwang/Documents/semester3/Analysis of Data from High-Throughput Molecular Biology Experiments/Project/Results_My/HeatMap/NC0102reporter_kegg_DESeq2_piano.xls")

gsaRes_HS_kegg2_2 <- runGSA(pv, fc, gsc=kegg, geneSetStat="tailStrength", 
                           nPerm=1000, verbose=TRUE)
GSAsummaryTable(gsaRes_HS_kegg2_2, save=TRUE, 
                file="/Users/xueqingwang/Documents/semester3/Analysis of Data from High-Throughput Molecular Biology Experiments/Project/Results_My/HeatMap/NC0102reporter_kegg_DESeq2_piano.xls")


gsaRes_HS_kegg3_1 <- runGSA(pv, fc, gsc=kegg, geneSetStat="fisher",
                          signifMethod="nullDist", nPerm=1000, verbose=TRUE)
GSAsummaryTable(gsaRes_HS_kegg3_1, save=TRUE, 
                file="/Users/xueqingwang/Documents/semester3/Analysis of Data from High-Throughput Molecular Biology Experiments/Project/Results_My/HeatMap/NC0102reporter_kegg_DESeq2_piano.xls")

gsaRes_HS_kegg3_2 <- runGSA(pv, fc, gsc=kegg, geneSetStat="fisher",
                          nPerm=1000, verbose=TRUE)
GSAsummaryTable(gsaRes_HS_kegg3_2, save=TRUE, 
                file="/Users/xueqingwang/Documents/semester3/Analysis of Data from High-Throughput Molecular Biology Experiments/Project/Results_My/HeatMap/NC0102reporter_kegg_DESeq2_piano.xls")


gsaRes_HS_kegg4_1 <- runGSA(pv, fc, gsc=kegg, geneSetStat="stouffer", 
                          signifMethod="nullDist", nPerm=1000, verbose=TRUE)
GSAsummaryTable(gsaRes_HS_kegg4_1, save=TRUE, 
                file="/Users/xueqingwang/Documents/semester3/Analysis of Data from High-Throughput Molecular Biology Experiments/Project/Results_My/HeatMap/NC0102reporter_kegg_DESeq2_piano.xls")

gsaRes_HS_kegg4_2 <- runGSA(pv, fc, gsc=kegg, geneSetStat="stouffer", 
                             nPerm=1000, verbose=TRUE)
GSAsummaryTable(gsaRes_HS_kegg4_2, save=TRUE, 
                file="/Users/xueqingwang/Documents/semester3/Analysis of Data from High-Throughput Molecular Biology Experiments/Project/Results_My/HeatMap/NC0102reporter_kegg_DESeq2_piano.xls")

resList <- list(gsaRes_HS_kegg1_1,gsaRes_HS_kegg1_2,gsaRes_HS_kegg2_2,
                gsaRes_HS_kegg3_1,gsaRes_HS_kegg3_2,gsaRes_HS_kegg4_1,gsaRes_HS_kegg4_2)
names(resList) <- c("reporter_nullDist","reporter","tailStrength",
                    "fisher_nullDist","fisher","stouffer_nullDist","stouffer")
#dev.off()
#par(mar=c(1,1,1,1))
ch <- consensusHeatmap(resList,cutoff=30,method="mean",ncharLabel = 100)
#nw <- networkPlot(gsaRes_HS_kegg,class="non")
#gsaRes_HS_go <- runGSA(pv,fc,gsc=go, geneSetStat="reporter", 
                       #signifMethod="nullDist", nPerm=1000, verbose=TRUE)
#par(mar = c(1,3,4,1.5))
##bottom,left,top,right
#nw <- networkPlot(gsaRes_HS_go, class="distinct", direction="both",
                  #significance=0.0002, label="numbers")
#nw$geneSets

#GSAsummaryTable(gsaRes_HS_go, save=TRUE, file="/Users/xueqingwang/Documents/semester3/Analysis of Data from High-Throughput Molecular Biology Experiments/Project/Results_My/HSnodu4_0102_go_DESeq2_piano.xls")
#gsaRes_HS_onco <- runGSA(pv, fc, gsc=onco, geneSetStat="reporter", 
#                          signifMethod="nullDist", nPerm=1000, verbose=TRUE)
#GSAsummaryTable(gsaRes_HS_onco, save=TRUE, file="/Users/xueqingwang/Documents/semester3/Analysis of Data from High-Throughput Molecular Biology Experiments/Project/Results_My/NCnodu2_onco_DESeq2_piano.xls")