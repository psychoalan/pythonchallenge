#!/usr/bin/python

# Example:
s = open('4.txt', 'r').read()

# Then you can print it:
#print linestring

#print len(linestring)

#print linestring[11]

for i in range(len(s)):
    
    
    if (s[i].islower()):	
        if (s[i+1].isupper()):
    
            if (s[i+2].isupper()):
                if (s[i+3].isupper()):
                    if (s[i+4].islower()):
	                if (s[i+5].isupper()):		
 			    if (s[i+6].isupper()):
 			        if (s[i+7].isupper()):
                                   	
                                    if (s[i+8].islower()):	
				        print s[i+4]






# You can even make a list with it!
#print linestring.split('\n')
