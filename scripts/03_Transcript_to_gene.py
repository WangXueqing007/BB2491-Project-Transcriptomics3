#=======================Create a dictionary oto match Ensembl transcripts and Ensembl genes.======================
f4=open('../Library/mart_export.txt','r')
num_line_f4=0
dic_transcript_gene={}
for line in f4:
    num_line_f4=num_line_f4+1
    if num_line_f4!=1:
        line=line.strip().split('\t')
        dic_transcript_gene[line[1]]=line[0]
#print(dic_transcript_gene,len(dic_transcript_gene))

f4.close()


#====================Write a new file, translate the transcripts in the 2nd-stage clean-up data to genes.
# Simply discard the transcripts which don not match to any genes.=====================
f5=open("../DATA/cleaned_data3.csv","r")
f6=open('../DATA/mapping_origin1.txt','w')
num_line_f5=0
for line in f5:
    num_line_f5=num_line_f5+1
    if num_line_f5==1:
        line=line.split(',')
        for i in line[0:len(line)-1]:
            f6.write(i+'\t')
        f6.write('\n')
    else:
        line=line.strip().split(',')
        if line [0] in dic_transcript_gene.keys():
            f6.write(dic_transcript_gene[line[0]]+'\t')
            for i in line[1:len(line)-1]:
                f6.write(i+'\t')
            f6.write(line[len(line)-1]+'\n')

f5.close()
f6.close()