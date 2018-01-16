
## Files description:
- cleaned_data_sample.tsv: The top 20 rows of the cleaned raw data.
- summed_mapdata_sample.tsv: The top 20 rows of DESeq2 input.
- DESeq2* files: The results of running DESeq2 on the mapped data.
- atlas_all* files: Adding HPA information to the original DESeq2 results, changing Ensebl name to gene name, filtering out the non-protein coding genes.
- atlasfiltered* files: Filetering out the high p-value-adj genes and reserving only the ones with p-value-adj<=0.05.
- Piano* files: The results of running Piano on HPA filtered DESeq2 results.