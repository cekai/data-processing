#! /usr/bin/env python

import re

line_list = []
with open('code.txt') as f:
	line_list = f.readlines()

line_list = [int(re.findall(r'[0-9]+[0-9]', line)[0]) for line in line_list]
print(sum(line_list))
