g=[]
k=[]

while True:
    s=(input("整数を入力："))
    if s=="":
        break
    else:
        s=int(s)
        if s%2==0:
            g.append(s)
        else:
            k.append(s)

for n in g:
    print("偶数:{} ".format(n),end="")
for n in k:
    print("奇数:{} ".format(n),end="")

