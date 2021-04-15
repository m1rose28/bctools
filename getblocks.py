import urllib.request
import re
from html.parser import HTMLParser

n=101

class getBlocks(HTMLParser):
    def handle_starttag(self, tag, attrs):
      if tag != 'a':
        return
      attr = dict(attrs)
      if 'rel' in attr.keys():
        if(attr['rel']=='next'):
          print("Next page:",attr['href'])
    def handle_data(self, data):
        isblock = re.search("00000", data)
        if(isblock):
          print(data)
          x = open("bcblockdata.txt", "a")
          x.write(str(n)+":"+str(data) + "\n")
          x.close()

parser = getBlocks()

while(n<500):
  url = "https://www.bitcloutpulse.com/explorer?page="+str(n)
  fp = urllib.request.urlopen(url)
  f = fp.read()
  f1 = f.decode("utf8")
  fp.close()
  parser.feed(f1)
  n +=1
