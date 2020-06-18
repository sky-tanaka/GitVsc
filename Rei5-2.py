list1=[]

while True:
    a=(input("数値を入力："))
    if a=="":
        break
    else:
        a=float(a)
        list1.append(a)

length=len(list1)
if length>0:
    min=list1[0]
    max=list1[0]

    sum=0.0

    for a in list1:
        print("{} ".format(a),end="")
        if max>a:
            max=a
        if min<a:
            min=a
        sum+=a

    avg=sum/length
    print()
    print("合計：{}　平均：{}　最大値：{}　最小値：{}".format(sum,avg,max,min))
