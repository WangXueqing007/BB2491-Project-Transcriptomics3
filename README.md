## Welcome to My Project Page of BB2491!

### Link to [Project Diary](https://github.com/WangXueqing007/BB2491-Project-Transcriptomics9/wiki)

### Project Description:
```markdown
Here the task is to investigate the difference in transcription data of Liver biopsies from Normal, Steatosis, NASH and HCC patients. 
Steatosis is a condition identified by liver enlargement and accumulation of lipids (in > 5% of hepatocytes), mostly without inflammation in the liver. 
Untreated steatosis can result in NASH (Non-Alcoholic Steatohepatitis), a more advanced condition (20-25% accumulation of fat in hepatocytes) identified by liver inflammation and can cause liver scarring. 
This condition can lead into a more severe problem such as irreversible cirrhosis and HCC, which is one of the deadliest and most common type of liver cancer.
The data consists of RNA-Seq raw count values from liver samples from in total 97 samples.
```

### Aims: 
```markdown
- Perform quality control and normalization of the data and identify the biological and technical replicates.
- Perform differential expression analysis to understand the transcriptional changes in each progression step.
- Analysis of the result and compare with previously published results and/or available resources such as Human Pathology Atlas.
```

### Tools:
```markdown
1. Programming languages: Python, R
2. Packages used:
- Pandas (python), DESeq2 (R), Piano (R), DAVID, PathwAX --directly
- Limma, ANOVA, Cytoscape --learned (or done by other members in the group), but didn't performed by myself
```

### Results:
```markdown
1. Cleaned-up data for DESeq2 and Piano.
2. DESeq2:
- Got the number of differentially expressed genes between each two adjacent stages, with FDR <= 5%;
- Volcano plot and t-SNE (Done by Dimitri);
3. ANOVA (Done by Mahammad).
4. Piano:
- Got the number of disturbed pathways and their statistics (including regulation directions), with FDR <= 5%;
- Literature searching, understanding the physiological meaning of the extracted pathways, validating our results with others' studies, and ruling out unreasonable pathways.
- Visualization (pathway networks and heatmaps among different settings of Piano)
5. DAVID/PathwAX: 
-  Got the number of disturbed pathways and their statistics. This part of results is not included in our poster.
```

