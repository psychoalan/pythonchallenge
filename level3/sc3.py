#!/usr/bin/python

with open('new.txt') as file_object:
    contents = file_object.read()
    x=set()
    x.add(contents.strip())
    print(x)    
    
