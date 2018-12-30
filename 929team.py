import csv
import re



#==============================================================================
# 处理个人数据集

jobcat={}
with open('resume_dataset.csv','r',encoding='UTF-8') as compaire:
    comp = csv.DictReader(compaire)
    column2 = [row['Category'] for row in comp]
    for line2 in column2: ##比较新建的counts库和这个人有没有counts 库内的数据 没有推荐剩余
        if line2 in jobcat:
                jobcat[line2] += 1
        else:
                jobcat[line2] = 1


a=filter(lambda x:x[1] in range(5), jobcat.items())
for key,value in list(a):
    del jobcat[key] #删除掉低频率项

# 处理公司数据集，找到对应职业信息    

#==============================================================================
# 处理公司数据集
with open('stoplist.txt','r',encoding='UTF-8') as f:
    stops = f.read()#stoplist.自己新建一个stoplist.txt,每次运行一遍下面程序去找无用的关键语句

# 处理个人数据集

indcat={}
with open('job_skills.csv','r',encoding='UTF-8') as compaire0:
    comp0 = csv.DictReader(compaire0)
    column1 = [row['Category'] for row in comp0]
    for line1 in column1: ##比较新建的counts库和这个人有没有counts 库内的数据 没有推荐剩余
        if line2 in indcat:
                indcat[line1] += 1
        else:
                indcat[line1] = 1


b=filter(lambda x:x[1] in range(5), indcat.items())
for key,value in list(b):
    del indcat[key] #删除掉低频率项

counts={}
with open('job_skills.csv','r',encoding='UTF-8') as csvfile:
    reader = csv.DictReader(csvfile)
    column = [row['Minimum Qualifications'] for row in reader]#选列名
    for line in column:
      if 'in ' in line:  
        word = re.compile(r'in (.*).')#目前最优的正则化语句
        line.replace(r'or',r',')#替换
        for wd in word.findall(line,re.S):
    #                if wd not in stops:
            if wd in counts:
                counts[wd] += 1
            else:
                counts[wd] = 1
pairs = sorted(counts, key=lambda v:counts[v], reverse=True)
print(pairs[:10]) #找前十


        
