l=[]

while True:
    s=input("単語を入力:")
    if s=="":
        break
    else:
        l.append(s)

for s in l:
    print("{}".format(s),end=" ")