
f1=open('../DATA/raw_counts.txt')
f2=open('../DATA/metadata_patient_code.txt')

#load = np.loadtxt('/DATA/metadata_patient_code.txt', skiprows=1)
#sample = np.asarray([row[1] for row in load])
#identifier = np.asarray([row[0] for row in load])

line_num_f2=0
dic_sample_id={}
#sample=[]
#identifier=[]

#=====================================Same as the first code, as a list of patient IDs is needed.=========================
for line in f2:
    line_num_f2=line_num_f2+1
    line=line.split()
    if line_num_f2!=1:
        dic_sample_id[line[0]]=line[1]
        #sample.append(line[0])
        #identifier.append(line[1])
del dic_sample_id['025'], dic_sample_id['T022'], dic_sample_id['008']
f2.close()

list_value=[]
for key,value in dic_sample_id.items():
    list_value.append(value)
#print("list_value =",list_value,",len(list_value) =",len(list_value))
set_value=set(list_value)
#print("set_value =",set_value,",len(set_value) =",len(set_value))

print ("The dictionary has been built. The number of samples is %s," % len(dic_sample_id), "the number of individuals is %s." % len(set_value))
print ('dic_sample_id=',dic_sample_id)
#print ('len(dic_sample_id)=',len(dic_sample_id))


#=============Statistics of the first-stage clean-up data: How many samples/individuals are repeated,
#  and how many times are they repeated for each?=====================================
cleaned = "../DATA/cleaned_data.csv" #where you want the file to be downloaded to

csv = open(cleaned, "r")
num_line=0
list_first_line=[]
for line in csv:
    if num_line==0:
        for element3 in line.strip().split(','):
            list_first_line.append(element3)
    num_line=num_line+1
print('list_first_line=',list_first_line)
print('len(list_first_line)=',len(list_first_line))

repeating_sample_list=[]
repeating_sample_set=set()
repeating_index_list=[]
repeating_index_set=set()
for index2,element4 in enumerate(list_first_line):
    #print(index2,element4)
    for index3 in range(0,index2,1):
        #print(index2,index3,list_first_line[index3],element4)
        if element4==list_first_line[index3]:
            repeating_index_list.append(index2)
            repeating_index_set.add(index2)
            repeating_sample_set.add(element4)
            repeating_sample_list.append(element4)
print ("The statistics of data: ")
print("The number of usable experiments is %s." % len(list_first_line))
print ("The number of repeated samples is %s." % len(repeating_index_list))
print("There are %s individuals being measured twice." % (len(repeating_sample_set)-(len(repeating_index_list)-len(repeating_index_set))))
print("There are %s individuals being measured three times." % (len(repeating_index_list)-len(repeating_index_set)))

#print(repeating_index_list,len(repeating_index_list))
#print(repeating_index_set,len(repeating_index_set))
#repeating_sample_set_list=list(repeating_sample_set)
three_samples=[]
for element5 in repeating_sample_set:
    count1=0
    for element6 in repeating_sample_list:
        if element6==element5:
            count1=count1+1
    if count1==3:
        three_samples.append(element5)
#print(repeating_sample_list,len(repeating_sample_list))
#print(repeating_sample_set,len(repeating_sample_set))
#print(repeating_sample_set_list,len(repeating_sample_set_list))
print("The elements that were repeated three times:",three_samples,"Number:",len(three_samples))

csv.close()

##===============As an continuation of the codes above; now that we have known the four individuals that have been repeated three times,
# we can simply specify them and their indices, for the aim of summing them up.==============================
indices_H010=[]
indices_S004=[]
indices_N009=[]
indices_N010=[]
dic_twice={}
for index4,element6 in enumerate(list_first_line):
    if element6=='H010':
        indices_H010.append(index4)
    elif element6=='S004':
        indices_S004.append(index4)
    elif element6=='N009':
        indices_N009.append(index4)
    elif element6 == 'N010':
        indices_N010.append(index4)
    else:
        for index5 in range(len(list_first_line)-1, index4, -1):
            if list_first_line[index5]==list_first_line[index4]:
                dic_twice[index4]=index5

print("Indices_H010=",indices_H010,"Indices_S004=",indices_S004,"Indices_N009=",indices_N009,"Indices_N010=",indices_N010)
print("dic_twice=",dic_twice,"Len(dic_twice)=",len(dic_twice))


##================Write into a new file, to sum up all the technical replicates
# and make sure that each individual shows up only once.===============================================
csv = open("../DATA/cleaned_data.csv", "r")
csv3=open("../DATA/cleaned_data3.csv","w")
num_line2=0
for line in csv:
    num_line2=num_line2+1
    line=line.split(',')
    row=str()
    #list_line1=[]
    if num_line2==1:
        for index6, element7 in enumerate(line):
            #if index6 in dic_twice.keys():
                #csv3.write(element7+'\t')
            if index6==indices_H010[0]:
                row=row+element7+','
            elif index6==indices_S004[0]:
                row = row + element7 + ','
            elif index6==indices_N009[0]:
                row = row + element7 + ','
            elif index6==indices_N010[0]:
                row = row + element7 + ','
            elif index6 not in dic_twice.values() and index6 not in indices_H010 and index6 not in indices_S004 and index6 not in indices_S004 and index6 not in indices_N009 and index6 not in indices_N010:
                row = row + element7 + ','
        csv3.write(row+'\n')
    else:
        for index6, element7 in enumerate(line):
            if index6 == indices_H010[0]:
                new_value=float(element7)+float(line[indices_H010[1]])+float(line[indices_H010[2]])
                csv3.write(str(new_value)+',')
            elif index6 == indices_S004[0]:
                new_value=float(element7)+float(line[indices_S004[1]])+float(line[indices_S004[2]])
                csv3.write(str(new_value)+',')
            elif index6 == indices_N009[0]:
                new_value=float(element7)+float(line[indices_N009[1]])+float(line[indices_N009[2]])
                csv3.write(str(new_value)+',')
            elif index6 == indices_N010[0]:
                new_value=float(element7)+float(line[indices_N010[1]])+float(line[indices_N010[2]])
                csv3.write(str(new_value)+',')
            elif index6 in dic_twice.keys():
                new_value = float(element7) + float(line[dic_twice[index6]])
                csv3.write(str(new_value) + ',')
            elif index6 not in dic_twice.values() and index6 not in indices_H010 and index6 not in indices_S004 and index6 not in indices_S004 and index6 not in indices_N009 and index6 not in indices_N010:
                csv3.write(element7 + ',')
        csv3.write('\n')

csv.close()
csv3.close()