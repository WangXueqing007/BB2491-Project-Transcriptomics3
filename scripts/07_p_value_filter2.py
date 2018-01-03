
#=================Filter out only the genes with p-value<=0.05.===========================

f1=open('../Results_My/atlas_all_NC_DESeq2.tsv','r')
f2=open('../Results_My/filtered_NC_DESeq2.tsv','w')
for num_line,line in enumerate(f1):
    if num_line==0:
        f2.write('\t'+line)
    else:
        line=line.strip().split('\t')
        if line[6]!='NA' and float(line[6])<=0.05:
            for i in range(0,len(line)-1):
                f2.write(line[i]+'\t')
            f2.write(line[len(line)-1]+'\n')
f1.close()
f2.close()

