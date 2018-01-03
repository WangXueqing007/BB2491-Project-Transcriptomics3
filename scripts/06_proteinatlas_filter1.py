
#===============Filter out the DESeq results that are protein-coding.========================

f_before=open('../Results_My/NC_DESeq2.tsv','r')
f_atlas=open('../Library/proteinatlas.tsv','r')
f_after=open('../Results_My/atlas_all_NC_DESeq2.tsv','w')

f_after.write('Gene'+"\t"+'RNA Tissue Category'+'\t'+'RNA TS TPM'+'\t'+'BaseMean'+'\t'+'log2FoldChange'+'\t'+'lfcSE'+'\t'+'stat'+'\t'+'P value'+'\t'+'P value adjusted'+'\n')

list_f_before=[]
for num_line2,line2 in enumerate(f_before):
    if num_line2!=0:
        line2 = line2.strip().split('\t')
        list_f_before.append(line2)
        #print(str(line2[0]))

for num_line1,line1 in enumerate(f_atlas):
    line1=line1.strip().split('\t')
    print("Processing line %s. Please be patient..." % num_line1)
    for element1 in list_f_before:
        #print(element1[0][1:17])
        if str(element1[0][1:16])==str(line1[2]):
            #print(element1[0])
            f_after.write(line1[0]+'\t'+line1[15]+'\t'+line1[17]+'\t'+element1[1]+'\t'+element1[2]+'\t'+element1[3]+'\t'+element1[4]+'\t'+element1[5]+'\t'+element1[6]+'\n')
f_before.close()
f_atlas.close()
f_after.close()