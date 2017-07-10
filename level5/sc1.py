#!/usr/bin/python

#except ImportError:
from urllib2 import urlopen

#u = urlopen("http://www.pythonchallenge.com/pc/def/chainsaw.jpg")
#u = urlopen("www.pythonchallenge.com/pc/def/linkedlist.php")
s = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"

s1 = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

u = urlopen(s)
#u = urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=44827")

data = u.readline()





#data = u.info()
for i in range(400):
    
    print data
#data2 = data[24]+data[25]+data[26]+data[27]
    data2 = data[-5:]
    print data2  

    s2 = s1 + data2
    u2 = urlopen(s2)
    datax = u.readline()

    print datax  
