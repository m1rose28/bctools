import json

n=1
x="000000000014abadcaf8f1853a3859bd0199db3313815e090ba76264b95d6c1d"

f = open(x, "r")
f1 = f.read()
f2 = str(f1)
f.close()

# parse x:
y = json.loads(f1)

# the result is a Python dictionary:
#print(y)
print(y["Header"])
print(y["Header"]["PrevBlockHashHex"])
print(y["Header"]["TstampSecs"])
print(len(y["Transactions"]))