# -*- coding: utf-8 -*-
"""preprocessing3_new.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZXsyHuHwYijKKQK5y2-ed1rYvYuMJrng
"""

from google.colab import drive

drive.mount('/content/gdrive')

import os
print(os.getcwd())
os.chdir("/content/gdrive/My Drive/Colab Notebooks/NewVersion")
print(os.getcwd())

import numpy as np
from collections import defaultdict
from sklearn.model_selection import train_test_split
import codecs


##########################################################
wikivoc={}
codewiki=defaultdict(list)

file2=codecs.open("wikipedia_knowledge_new",'r','utf-8')
line=file2.readline()
count=0
while line:
    if line[0:4]=='XXXd':
        line=line.strip('\n')
        line=line.split()
        for i in line:
            if i[0:2]=='d_':
                codewiki[i].append(count)
                wikivoc[i]=1
        count=count+1
    line=file2.readline()

################### four codes have two wikidocuments, correct them
codewiki['d_072']=[214]
codewiki['d_698']=[125]
codewiki['d_305']=[250]
codewiki['d_386']=[219]
np.save('wikivoc_new',wikivoc)

filec=codecs.open("combined_dataset",'r','utf-8')

line=filec.readline()

feature=[]
label=[]

while line:
    line=line.strip('\n')
    line=line.split()
    
    if line[0]=='codes:':
        temp=line[1:]
        label.append(temp)
        line=filec.readline()
        line=line.strip('\n')
        line=line.split()
        if  line[0]=='notes:':
            tempf=[]
            line=filec.readline()
           
            while line!='end!\n':
                line=line.strip('\n')
                line=line.split()
                tempf=tempf+line
                line=filec.readline()
            feature.append(tempf)
    line=filec.readline()


prevoc={}
for i in label:
    for j in i:
        if j not in prevoc:
            prevoc[j]=len(prevoc)

notevec=np.load('notevec_new.npy')
wikivec=np.load('wikivec_new.npy')
label_to_ix = {}
ix_to_label={}


for codes in label:
    for code in codes:
        if code not in label_to_ix:
            label_to_ix[code]=len(label_to_ix)
            ix_to_label[label_to_ix[code]]=code

tempwikivec=[]

for i in range(0,len(ix_to_label)):
    if ix_to_label[i] in wikivoc:
        temp=wikivec[codewiki[ix_to_label[i]][0]]
        tempwikivec.append(temp)
    else:
        tempwikivec.append([0.0]*wikivec.shape[1])
wikivec=np.array(tempwikivec)

####################################

data=[]
for i in range(0,len(feature)):
    data.append((feature[i], notevec[i], label[i]))
    
data=np.array(data)  

label_to_ix = {}
ix_to_label={}

for doc, note, codes in data:
    for code in codes:
        if code not in label_to_ix:
            if code in wikivoc:
                label_to_ix[code]=len(label_to_ix)
                ix_to_label[label_to_ix[code]]=code

np.save('label_to_ix_new',label_to_ix)
np.save('ix_to_label_new',ix_to_label)

training_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
training_data, val_data = train_test_split(training_data, test_size=0.125, random_state=42)

np.save('training_data_new',training_data)
np.save('test_data_new',test_data)
np.save('val_data_new',val_data)

word_to_ix = {}
ix_to_word={}
ix_to_word[0]='OUT'


for doc, note, codes in training_data:
    for word in doc:
        if word not in word_to_ix:
            word_to_ix[word] = len(word_to_ix)+1
            ix_to_word[word_to_ix[word]]=word  
    
np.save('word_to_ix_new',word_to_ix)
np.save('ix_to_word_new',ix_to_word)

newwikivec=[]
for i in range(0,len(ix_to_label)):
    newwikivec.append(wikivec[prevoc[ix_to_label[i]]])
newwikivec=np.array(newwikivec)
np.save('newwikivec_new',newwikivec)

print(len(codewiki))
print(len(prevoc))
print(len(feature))
print(len(label))
print(len(wikivec))
print(len(label_to_ix))
print(len(ix_to_label))
print(data.shape)
print(training_data.shape)
print(test_data.shape)
print(val_data.shape)
print(len(newwikivec))

"""Wikipedia pages available for the first three digits ICD-9 diagnosis codes = `len(codewiki)` = 389

The code vocabulary = `len(prevoc)` = 941

Total number of aggregated discharge notes (per patient) = 52722 

Number of Wikipedia vectors = `len(wikivec)` = 344

Number of data sample = `data.shape` = 52722

Number of samples in training data = `training_data.shape` 36904

Number of samples in test data = `test_data.shape` 10545

Number of samples in validation data = `val_data.shape` = 5273

"""