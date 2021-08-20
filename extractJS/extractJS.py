#!/bin/python3
#This program is built by Dev_Ali.
#The purpose of this program is to extract all the JavaScript links from a file. 
#The program comes handy when people like developers and hackers etc want to extract Javascript file links from source codes for performing further operation. 

import re
import sys

#File Handler
file = input("Enter a filename: ")
try:
    handle = open(file)
except:
    print("File not found!")
    sys.exit()

#Extract js links
links = list()
for lines in handle:
    search = re.findall("https://\S+js", lines)
    if len(search) < 1:
        continue
    else:
        for value in search:
            links.append(value)

#Output
count = 0
for link in links:
    count = count + 1
    print(count, "-", link)
print("The total number of links extracted is", count)

