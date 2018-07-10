import pandas as df
import numpy as np

def get_train():
    dataset_file_name_train = './train_total_annotated_set_category.csv'
    dataset_read_train = df.read_csv(dataset_file_name_train)
    dataset_titles_train = dataset_read_train['title'].values
    dataset_labels_train = dataset_read_train['Classification'].values
    dataset_cat_train = dataset_read_train['Category'].values

    titles = []
    for i in range(len(dataset_titles_train)):
        if dataset_labels_train[i] == '?':
            print("Skipped at index", i)
        else:
            titles.append(dataset_titles_train[i].lower().replace('-',''))

    titles_non_nan = []
    labels_non_nan = []
    cat_non_nan = []
    for i in range(len(titles)):
        if type(dataset_cat_train[i]) == str:
            titles_non_nan.append(titles[i])
            labels_non_nan.append(dataset_labels_train[i])
            cat_non_nan.append(dataset_cat_train[i])
        else:
            continue


    categories_set = list(set(cat_non_nan))

    nummed_categories = [0 for j in titles_non_nan]

    for i in range(len(nummed_categories)):
        nummed_categories[i] = categories_set.index(cat_non_nan[i])

    labels = []
    for i in range(len(titles_non_nan)):
        label = [0 for j in categories_set]
        label[nummed_categories[i]] = 1
        labels.append(label)
    y = np.array(labels)
    
    return titles_non_nan, labels_non_nan, cat_non_nan, y

def get_test():
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

    for i in range(len(nummed_categories)):
        nummed_categories[i] = categories_set.index(cat_non_nan[i])

    labels = []
    for i in range(len(titles_non_nan)):
        label = [0 for j in categories_set]
        label[nummed_categories[i]] = 1
        labels.append(label)
    y = np.array(labels)
    
    return titles_non_nan, labels_non_nan, cat_non_nan, y

titles_train, _, _, y_train = get_train()
titles_test, _, _, y_test = get_test()
