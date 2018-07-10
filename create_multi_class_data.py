import numpy as np
import re
import data_helpers
import tensorflow as tf
import numpy as np
import os
import time
import datetime
import yaml
import math
import pandas as df

dataset_file_name_test = './test_total_annotated_set_category.csv'
dataset_read_test = df.read_csv(dataset_file_name_test)
dataset_titles_test = dataset_read_test['title'].values
dataset_labels_test = dataset_read_test['Classification'].values
dataset_cat_test = dataset_read_test['Category'].values

titles = []
for i in range(len(dataset_titles_test)):
    if dataset_labels_test[i] == '?':
        print("Skipped at index", i)
    else:
        titles.append(dataset_titles_test[i].lower().replace('-',''))

titles_non_nan = []
labels_non_nan = []
cat_non_nan = []
for i in range(len(titles)):
    if type(dataset_cat_test[i]) == str:
        titles_non_nan.append(titles[i])
        labels_non_nan.append(dataset_labels_test[i])
        cat_non_nan.append(dataset_cat_test[i])
    else:
        continue
        

categories_set = list(set(cat_non_nan))

nummed_categories = [0 for j in titles_non_nan]

for i in range(len(nummed)):
    nummed_categories[i] = categories_set.index(cat_non_nan[i])

nummed_categories = [0 for j in titles_non_nan]

for i in range(len(nummed)):
    nummed_categories[i] = categories_set.index(cat_non_nan[i])

labels = []
for i in range(len(titles_non_nan)):
    label = [0 for j in categories_set]
    label[nummed_categories[i]] = 1
    labels.append(label)
y = np.array(labels)

#categories_set

#print(cat_non_nan[247])
#print(y[247])
