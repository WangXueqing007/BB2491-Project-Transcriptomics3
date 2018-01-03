f1=open('../Results_My/atlas_all_HS_DESeq2.tsv','r')
list_line=[]
set_line=set()
for line in f1:
    line=line.strip().split('\t')
    list_line.append(line[0])
set_line=set(list_line)
print("list_line=",list_line)
print("set_line=",set_line)
print(len(list_line),len(set_line))