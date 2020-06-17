for a in range(2,101):
    count=0
    for b in range(1,a+1):
        if a%b==0:
            count=count+1
    if count==2:
        print("{} ".format(a),end="")

