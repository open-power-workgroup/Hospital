import sys,os,csv

iFile=open('./raw.in','rU')
jFile=open('result.csv','w')
root="root-kepler186f"

sour=iFile.readlines()

source_list=[]
carry_dict={}
for line in sour:
    current=line.replace('\n','')
    if current.find("##")>-1 or current.find("#")>-1:
        #this is title
        titletext=current.strip(' ').split(' ')[1].replace('/','-')
        carry_dict[titletext]=[]
    elif current.find("-")>-1:
        subtext=current.strip(' ').split(' ')[1]
        if subtext not in carry_dict[titletext]:
            carry_dict[titletext].append(subtext)


print carry_dict

jFile.write('id,value\n')
jFile.write(root+',\n')
for key in carry_dict:
    jFile.write(root+'.'+key+',\n')
    for item in carry_dict[key]:
        jFile.write(root+'.'+key+'.'+item+',1\n')



iFile.close()
iFile.close()