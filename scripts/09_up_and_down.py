#==========Rewrite Dimitri's Piano results for the ease of pathway analyzation (Literature searching).======================
import pandas as pd

f1=open('../Results-Dimitri/Piano_summary_kegg_NC.txt','r')
f2=open('../Results-Dimitri/Piano_summary_go_NC.txt','r')
writer = pd.ExcelWriter('../Results-Dimitri/Piano2_summary_NC.xlsx')


big_list_up1=[]
big_list_down1=[]
for num_line1,line1 in enumerate(f1):
    line1=line1.strip().split('\t')
    if num_line1==0:
        big_list_up1.append(line1)
        big_list_down1.append(line1)
    elif line1[1]=='UP':
        big_list_up1.append(line1)
    elif line1[1]=='DOWN':
        big_list_down1.append(line1)

big_array_up1=pd.DataFrame(big_list_up1)
big_array_down1=pd.DataFrame(big_list_down1)

big_list_up2=[]
big_list_down2=[]
for num_line2,line2 in enumerate(f2):
    line2=line2.strip().split('\t')
    if num_line2==0:
        big_list_up2.append(line2)
        big_list_down2.append(line2)
    elif line2[1]=='UP':
        big_list_up2.append(line2)
    elif line2[1]=='DOWN':
        big_list_down2.append(line2)

big_array_up2=pd.DataFrame(big_list_up2)
big_array_down2=pd.DataFrame(big_list_down2)

f1.close()
f2.close()

big_array_up1.to_excel(writer,'KEGG_UP')
big_array_down1.to_excel(writer,'KEGG_DOWN')
big_array_up2.to_excel(writer,'GO_UP')
big_array_down2.to_excel(writer,'GO_DOWN')

