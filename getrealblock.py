import urllib.request
import json

n=1
x="00000000000c957209742129b3d139fa2478232a6e0552d49886183d06768923"
key = "01d77ef8-1b66-4b5a-b7c6-3cbf7b9e791e"

while(n<1000):
  url = "https://www.bitcloutapi.net/api/blocks/"+x+"?key="+key
  fp = urllib.request.urlopen(url)
  f = fp.read()
  f1 = f.decode("utf8")
  fp.close()
  fx = open("blocks/"+x, "w")
  fx.write(f1)
  fx.close()

  f2 = str(f1)
  y = json.loads(f2)
  x=y["Header"]["PrevBlockHashHex"]
  ts = str(y["Header"]["TstampSecs"])
  n +=1
  txn = str(len(y["Transactions"]))
  print(str(n) + " : "+ txn + " transactions @ " + ts)
  print(x)
