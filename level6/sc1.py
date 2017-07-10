#!/usr/bin/python

import cPickle
from urllib2 import urlopen

s = "http://www.pythonchallenge.com/pc/def/banner.p"
u = urlopen(s)
data = u.read()
#data = u.readline()
#print data
text = cPickle.dumps(data)
# or to binary 
bytes = cPickle.dumps(data,2)
#print text
#redata1 = cPickle.loads(text)
#print redata1
#print bytes

def containsAny(text, aset):
    for item in itertools.ifilter(aset.__contains__,text):
        return True
        print item
    return False

newstr = text.replace("n", "")
newst = newstr.replace("\\", "")
#result.replace("\\", "") 
print newst
