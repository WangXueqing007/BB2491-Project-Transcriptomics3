f6=open('../DATA/mapping_origin1.csv','r')
f7=open('../DATA/mapping2.csv','w')

gene_name=[]
num_line_f6=0
dic_num_line={}
for line in f6:
    num_line_f6=num_line_f6+1
    list_line_f6=line.strip().split(',')
    dic_num_line[num_line_f6] = list_line_f6
    gene_name.append(list_line_f6[0])
    if num_line_f6==1:
        f7.write(line+'\n')


for index8 in range (1,len(gene_name)):
    if dic_num_line [index8][0] not in gene_name[0:index8]:
        f7.write(dic_num_line[index8][0]+',')
        total01=[]
        for i1 in dic_num_line [index8][1:len(list_line_f6)]:
            float_count1=float(i1)
            total01.append(float_count1)
        for num1 in range(index8,len(gene_name),1):
            if gene_name[num1]==dic_num_line[index8][0]:
                for num2 in range(0,len(total01)):
                    total01[num2]=total01[num2]+float(dic_num_line[num1][num2+1])
        for i2 in range(0,len(total01)-1):
            f7.write(str(total01[i2])+'\t')
        f7.write(str(total01[len(total01)-1]),',')
f6.close()
f7.close()