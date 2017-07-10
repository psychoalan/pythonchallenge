#!/usr/bin/python

# Example:
s = open('4.txt', 'r').read()

# Then you can print it:
#print linestring

#print len(linestring)

#print linestring[11]

for i in range(len(s)):
    if (s[i].isupper()):
        if (s[i+1].isupper()):
            if (s[i+2].isupper()):
                if (s[i+3].islower()):
	            if (s[i+4].isupper()):		
 			if (s[i+4].isupper()):
 			    if (s[i+4].isupper()):	
				print s[i+3]






# You can even make a list with it!
#print linestring.split('\n')
