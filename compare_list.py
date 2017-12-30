import csv
from collections import defaultdict


columns = defaultdict(list)

with open('compare_list.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for (colname, email) in row.items():
            columns[colname].append(email)

emails_1 = columns['Emails_1']
emails_2 = columns['Emails_2']

emails_2 = filter(None, emails_2)
emails_1 = filter(None, emails_1)

duplicates1 = set([x for x in emails_1 if emails_1.count(x) > 1])
duplicates2 = set([x for x in emails_2 if emails_2.count(x) > 1])

if len(duplicates1) > 0:
    print("There are duplicate emails in email list #1")
if len(duplicates2) > 0:
    print("There are duplicate emails in email list #2")
    
#remove duplicates

a = set(emails_1)
b = set(emails_2)

#see difference
diff = a.symmetric_difference(b)
