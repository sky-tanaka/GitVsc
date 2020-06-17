a=1
#範囲指定あるからa=1,b=1およびa=a+1,b=b+1いらない
for a in range(1,10):
    b=1
    for b in range(1,10):
        print("{}×{}={:2} ".format(a,b,a*b),end="")
        b=b+1
    print()
    a=a+1
