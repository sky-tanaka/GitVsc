a=2
while a<=100:
    count=0
    b=1
    while b<=a:
        if a%b==0:
            count=count+1
        b=b+1
    if count==2:
        print("{} ".format(a),end="")
    a=a+1
