#!/usr/bin/python

from urllib2 import urlopen

s = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"

ss = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

u = urlopen(s)

data = u.readline()




for i in range(400):
     
     
     data = data[-5:]     
     if data[0].isspace():
         data = data[-4:]
     if data == '61287':
         data = '559'
     if data == '16044':
         data = '8022'
     if data == '82682':
         data = '63579'
     if data == '47769':
         data = '631'
     print data
     s = ss + data   
     u = urlopen(s)
     data = u.readline()
     
          
     #data = data[-5:]
     #print data






