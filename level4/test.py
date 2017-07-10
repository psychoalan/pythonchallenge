#!/usr/bin/python

s="AaAaA"

#print len(s)

for i in range(0,50):
    if s[i].isupper():
        print s[i]    
        if s[i+1].islower():
            #print s[i]
            print s[i] + s[i+1] 
            #i = i+1
            if s[i+2].isupper():
                print s[i] + s[i+1] + s[i+2]
                i = i + 1 
#for i in s:
#    print i
