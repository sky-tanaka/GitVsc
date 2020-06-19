def clac(a,b):
    ans1=a+b
    ans2=a-b
    ans3=a*b
    ans4=a//b

    return ans1,ans2,ans3,ans4

x=10
y=2

a1,a2,a3,a4=clac(x,y)

print("{}+{}={}".format(x,y,a1))
print("{}-{}={}".format(x,y,a2))
print("{}×{}={}".format(x,y,a3))
print("{}÷{}={}".format(x,y,a4))