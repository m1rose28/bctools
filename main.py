import re
import collections as col

#create bitcould chain NamedTuple and import data
block = col.namedtuple('block', ['date','time'])
B={}
N=[]

n=0
f = open("blocks.csv", "r")
for line in f:
  n =+ 1
  ls = line.strip()
  bx=re.split(",",ls)
  B[bx[1]] = block(bx[3],bx[4])
  #print(B[bx[1]])
f.close()

n=0
f = open("names.csv", "r")
for line in f:
  n =+ 1
  ls = line.strip()
  nx=re.split(",",ls)
  N.append(nx[1])
f.close()
#print(N[50])

f = open("bcs1.txt", "r")

lines=0
txn=0
like=0
post=0
creatorcoin=0
follow=0
bitcoinexchange=0
updateprofile=0
basictransfer=0
privatemessage=0

for line in f:
    ls = line.strip()
    istxn = re.search("TxnType", ls)
    if(istxn):
      txn +=1;
      #print(ls)
      islike = re.search("LIKE", ls)
      if(islike):
        like += 1
      iscreatorcoin = re.search("CREATOR_COIN", ls)
      if(iscreatorcoin):
        creatorcoin += 1
      isfollow = re.search("FOLLOW", ls)
      if(isfollow):
        follow += 1
      isbitcoinexchange = re.search("BITCOIN_EXCHANGE", ls)
      if(isbitcoinexchange):
        bitcoinexchange += 1
      isupdateprofile = re.search("UPDATE_PROFILE", ls)
      if(isupdateprofile):
        updateprofile += 1
      isbasictransfer = re.search("BASIC_TRANSFER", ls)
      if(isbasictransfer):
        basictransfer += 1
      isprivatemessage = re.search("PRIVATE_MESSAGE", ls)
      if(isprivatemessage):
        privatemessage += 1
      ispost = re.search("SUBMIT_POST", ls)
      if(ispost):
        post += 1
    lines += 1

f.close()
print("lines: ",lines)
print("transactions: ",txn)
print("posts: ",post)
print("creatorcoin: ",creatorcoin)
print("follow: ",follow)
print("bitcoinexchange: ",bitcoinexchange)
print("privatemessage: ",privatemessage)
print("updateprofile: ",updateprofile)
print("basictransfer: ",basictransfer)


#print(f.read())
