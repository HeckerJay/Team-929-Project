import csv
import re

#==============================================================================
# treat individuals' dataset， find out corresponded categories
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
    
#==============================================================================
# treat companies' dataset， find out corresponded categories
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
        finalcat.append(aimcat) #check the same categories dataset between two .csv
        
#==============================================================================
#creat a skill library from company's requirenment
with open('stoplist.txt','r',encoding='UTF-8') as f:
    stops = f.read() # get stoplist.


counts={}
with open('job_skills.csv','r',encoding='UTF-8') as csvfile:
    reader = csv.DictReader(csvfile)
    column = [row['Minimum Qualifications'] for row in reader] #select ideal needs 
    for line in column:
      if 'in ' in line:  
        word = re.compile(r'.*, (.*).*,') #RE compile
        line=line.replace(r'in ',r', ')
        line=line.replace(r'.',r', ')
        line=line.replace(r')',r', ')
        line=line.replace('and ',r', ')
        line=line.replace('or ',r', ') #replace symbol of keyword's position
        for wd in word.findall(line):
          if wd not in stops: #use stoplist to avoid unexcepted info
            if wd in counts:
                counts[wd] += 1
            else:
                counts[wd] = 1
pairs = sorted(counts, key=lambda v:counts[v], reverse=True)
pairs = pairs[:15]#find out most 15 frequent skills

#==============================================================================
#Compare the skills between individuals' resume and company's needs. Recommand related skill to learn.
comprow=[]
with open('resume_dataset.csv','r',encoding='UTF-8') as csvfile:
    comp = csv.DictReader(csvfile)
    for row in comp:
        if row['Category'] == 'Information Technology':
            comprow.append(row['ID'])
            
recomdlesson={}
with open('resume_dataset.csv','r',encoding='UTF-8') as csvfile:
    comp = csv.DictReader(csvfile)
    for row in comp:
        if row['ID'] in comprow:
            recomdlesson[row['ID']]='Recommended Lesson: '
            for check in pairs:
                recless=re.compile(r''+check+'')
                if recless.findall(row['Resume'])==[]:
                        recomdlesson[row['ID']]+=check+';'


with open('recommanded_lessons.csv','w+') as recom:
     w=csv.writer(recom)
     for key,value in recomdlesson.items():
         w.writerow([key,value])
