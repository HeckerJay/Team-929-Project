import csv
import re



#==============================================================================
# treat individuals' dataset

indcat={}
with open('resume_dataset.csv','r',encoding='UTF-8') as compaire:
    comp = csv.DictReader(compaire)
    column2 = [row['Category'] for row in comp]
    for line2 in column2:           
        if line2 in indcat:
                indcat[line2] += 1
        else:
                indcat[line2] = 1


a=filter(lambda x:x[1] in range(5), indcat.items())
for key,value in list(a):
    del indcat[key] #delete redundant information

# treat companies' dataset，find out corresponded categories

#==============================================================================
# 处理公司数据集
with open('stoplist.txt','r',encoding='UTF-8') as f:
    stops = f.read() # get stoplist.



jobcat={}
with open('job_skills.csv','r',encoding='UTF-8') as compaire0:
    comp0 = csv.DictReader(compaire0)
    column1 = [row['Category'] for row in comp0]
    for line1 in column1: 
        if line1 in jobcat:
                jobcat[line1] += 1
        else:
                jobcat[line1] = 1


b=filter(lambda x:x[1] in range(5), jobcat.items())
for key,value in list(b):
    del jobcat[key] #delete redundant information


finalcat=[]
for aimcat in  jobcat:
    if aimcat in indcat:
        finalcat.append(aimcat)
        
#==============================================================================
#比较新建的counts库和这个人有没有counts 库内的数据 没有推荐剩余        
counts={}
with open('job_skills.csv','r',encoding='UTF-8') as csvfile:
    reader = csv.DictReader(csvfile)
    column = [row['Minimum Qualifications'] for row in reader]#选列名
    for line in column:
      if 'in ' in line:  
        word = re.compile(r'in (.*).')#目前最优的正则化语句
        line.replace(r'or',r',')#替换
        for wd in word.findall(line,re.S):
    #                if wd not in stops:#use stoplist to avoid unexcepted info
            if wd in counts:
                counts[wd] += 1
            else:
                counts[wd] = 1
pairs = sorted(counts, key=lambda v:counts[v], reverse=True)
print(pairs[:10]) #find out most 10 frequent skills
        

        

        
