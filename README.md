## Welcome to My Project Page of BB2491!


### Project Description:
Here the task is to investigate the difference in transcription data of Liver biopsies from Normal, Steatosis, NASH and HCC patients. Steatosis is a condition identified by liver enlargement and accumulation of lipids (in > 5% of hepatocytes), mostly without inflammation in the liver. Untreated steatosis can result in NASH (Non-Alcoholic Steatohepatitis), a more advanced condition (20-25% accumulation of fat in hepatocytes) identified by liver inflammation and can cause liver scarring. This condition can lead into a more severe problem such as irreversible cirrhosis and HCC, which is one of the deadliest and most common type of liver cancer.
The data consists of RNA-Seq raw count values from liver samples from in total 97 samples.

### Aims: 
- Perform quality control and normalization of the data and identify the biological and technical replicates.
- Perform differential expression analysis to understand the transcriptional changes in each progression step.
- Analysis of the result and compare with previously published results and/or available resources such as Human Pathology Atlas.

### Tools:
```markdown
1. Programming languages: Python, R
2. Packages used:
- Pandas (python), DESeq2 (R), Piano (R) --directly
- Limma, David, ANOVA --learned (or done by other members in the group), but didn't performed by myself
```

### Results:
```markdown
1. Cleaned-up data for DESeq2 and Piano.
2. DESeq2:
- Got the number of differentially expressed genes between each two adjacent stages, with FDR <= 5%;
- Volcano plot and t-SNE (Done by Dimitri);
3. ANOVA (Done by Mahammad).
4. Piano:
- Got the number of changed pathways and their statistics, with FDR <= 5%;
- Literature searching, understanding the physiological meaning of the extracted pathways, validating our results with others' studies, and ruling out unreasonable pathways.
- Visualization (pathway networks and heatmaps among different settings of Piano)
```

###Links within my project:
[Project Diary](https://github.com/WangXueqing007/BB2491-Project-Transcriptomics9/wiki)

You can use the [editor on GitHub](https://github.com/WangXueqing007/BB2491-Project-Transcriptomics3/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/WangXueqing007/BB2491-Project-Transcriptomics3/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
