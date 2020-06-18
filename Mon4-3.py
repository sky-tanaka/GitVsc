a=int(input("1つ目の値：　"))
b=int(input("2つ目の値：　"))

if a<b:
    for a in range(a,b+1):
        print("{} ".format(a),end="")
elif a>b:
    for b in range(a,b-1,-1):
        print("{} ".format(b),end="")
else:
    print("異なる値を入力してください")

