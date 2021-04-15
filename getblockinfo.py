import urllib.request
from html.parser import HTMLParser
import re

n=0
dx1=0
zz=0

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        isTime = re.search("UTC", data)
        if(isTime):
          dx1=data
          dx1 = dx1.replace("  ", " ")
          dx1 = dx1.replace("  ", "")
          g = open("bcblockdata1.txt", "a")
          g.write(str(x[0]) + ":" + str(x[1]) + ":" + str(dx1) + "\n")
          g.close()

parser = MyHTMLParser()

def gDate(b):
  url = "https://www.bitcloutpulse.com/explorer/blocks/"+b
  fp = urllib.request.urlopen(url)
  f = fp.read()
  f1 = f.decode("utf8")
  fp.close()
  parser.feed(f1)

f = open("bcblockdata.txt", "r")

for line in f:
  n +=1
  print(n)
  #if(n>5):
  #  exit()
  ls = line.strip()
  x = ls.split(":")
  if(x[1]=="00000000000f34daa505aa85616735a9ba788067308ab597b85b24ff9ae35d15"):
    zz=1
  if(zz==1):
    x1 = gDate(x[1])



