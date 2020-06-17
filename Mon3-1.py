a=int(input("一つ目の整数："))
b=int(input("二つ目の整数："))

t=print("足し算{}".format(a+b))
h=print("引き算{}".format(a-b))
k=print("掛け算{}".format(a*b))

if b==0:
    print("0での割り算はできません")
else:
    print("割り算{}".format(a/b))
