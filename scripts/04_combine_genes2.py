#====================Combine the same gene to a single row.==============================
import pandas as pd

#data = pd.read_csv('../DATA/mapping_origin1.csv', keep_default_na=False, na_values=[""])
data = pd.read_table("../DATA/mapping_origin1.txt", index_col=0, header=0)
data = data.groupby(data.index, sort=True).sum()
data = data.T.groupby([s.split('.')[0] for s in data.T.index.values]).sum().T
data.to_csv(path_or_buf="../DATA/mapping2.tsv", sep='\t')