#!/usr/bin/python

with open('3.txt') as file_object:
    contents = file_object.read()
    x=set()
    x.add(contents)    
    print(x)
    
