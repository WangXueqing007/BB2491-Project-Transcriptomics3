f1=open('../DATA/raw_counts.txt')
f2=open('../DATA/metadata_patient_code.txt')


line_num_f2=0
dic_sample_id={}

#========================Make a dictionary of the metadata patient code, delete the low-quality ones.================
for line in f2:
    line_num_f2=line_num_f2+1
    line=line.split()
    if line_num_f2!=1:
        dic_sample_id[line[0]]=line[1]

del dic_sample_id['025'], dic_sample_id['T022'], dic_sample_id['008']
print ("The dictionary has been built. The number of samples is %s." % len(dic_sample_id))
f2.close()


#===========================Write all the raw count data into a huge list.=============================================
line_num_f1=0
huggge_list=[]
for line in f1:
    list_of_line=[]
    line = line.split()
    line_num_f1=line_num_f1+1
    if line_num_f1==1:
        index=[]
        list_of_line.append('TranscriptID')
        for count,element in enumerate(line):
            for key, value in dic_sample_id.items ():
                if key == element:
                    list_of_line.append(value)
                    index.append(count)
    else:
        list_of_line.append(line[0])
        for i in range(0,len(line)):
            if i in index:
                list_of_line.append(line[i])
    huggge_list.append(list_of_line)
f1.close()


#=======================Write the first-stage clean-up output: patient codes are used instead of sample code.
# Low-quality samples are removed.===========================================================
##example of writing data to a CSV file.

cleaned = "../DATA/cleaned_data.csv" #where you want the file to be downloaded to
csv = open(cleaned, "w")
#"w" indicates that you're writing strings to the file

for element2 in huggge_list:
    name0 = element2[0]
    row = name0 + ","
    for num1 in range(1,125):
        globals()['name%s' % num1] = element2[num1]
        row=row+globals()['name%s'%num1]+','
    name125 = element2[125]
    row = row + name125 + "\n"
    csv.write(row)

csv.close()
