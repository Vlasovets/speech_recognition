# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import os
import re
import numpy as np

colnames = ['file_name']
for i in range(1,6375):
    colnames.insert(i,'x')
test = pd.read_csv('~/Desktop/opensmile-2.3.0/project1/test.csv', names=colnames, header=None, sep= ',')    
#test = pd.read_csv('project/train_1580.csv', sep= ',')
label = pd.read_csv('~/Desktop/opensmile-2.3.0/project/test_label.tsv', sep= '\t')

    
# we remove the format name from the labels

label['file_name'] = label['file_name'].str.replace('.wav', '')

#drop unnecessary column of ID

#label_1 = label.drop(['promptId'], axis = 1)
label_1 = label


#change the name of the csv column to file_name' to be able to merge
test = test.drop('x.6373', axis=1)

test = test.rename(columns={x:y for x,y in zip(test.columns,range(0,len(test.columns)))})
dict_1 = test.to_dict('r')
new_test = pd.DataFrame(dict_1)

new_test.columns = ['file_name' if x==0 else x for x in new_test.columns]



label_1 = label_1.merge(new_test, on =['file_name'], how='left')
#output = new_test.merge(label_1, on = ['file_name'], how = 'left')


L1 = label_1["L1"]
label_1 = label_1.drop(['L1'], axis = 1)
label_1 = pd.concat([label_1, L1], axis=1)

#rewsult = label_1[3300::]



#result = pd.DataFrame(result,header=None)

#result = label_1.drop(label_1.index[3300::])

result = label_1

result.to_csv('~/Desktop/opensmile-2.3.0/Results/test.csv', header=None, index=False)


a = result.reset_index()
a = a.drop(['index'], axis=1)

a.to_csv('~/Desktop/opensmile-2.3.0/Results/test_header.csv')




# make a new column whci hcontains both vector and the label
label_1['vector_label'] = label[['L1',test.iloc[:,1::]]].max(axis=1)

 #drop unnecessary columns
label_1 = label.drop([['L1', test.iloc[:,1::]]], axis = 1)


#transponse to the format of OpenSmile
label_1 = label_1.T
