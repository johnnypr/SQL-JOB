#!/usr/bin/env python3

import pandas as pd

csv_file = open('/Users/johnnyperez/Desktop/SQL JOB/Projects/PROJECT 4/COMPANY.txt',encoding='utf-16')
# csv_file = open('/Users/johnnyperez/Desktop/SQL JOB/Projects/PROJECT 4/test2.txt')


new_file = open('/Users/johnnyperez/Desktop/SQL JOB/Projects/PROJECT 4/test.txt','w+')

def remove_values_from_list(the_list, val):
       return [value for value in the_list if value != val]

for row in csv_file:
    row = row.split("\"\"")
    row = remove_values_from_list(row,',')
    row = [row[x] for x in range(1,len(row))]
    for col in row:
        col = "\"" + col + "\"" + ','
        new_file.write(col)
new_file.close()
