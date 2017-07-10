#!/usr/bin/python

with open('3.txt') as file_object:
    for line in file_object:
        cleanedLine = line.strip()
        if cleanedLine:
            #print(cleanedLine)
            x=set()
            x.add(cleanedLine)
            print(x)    
    
