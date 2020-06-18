a=int(input("1つ目の値：　"))
b=int(input("2つ目の値：　"))
if a<b:
    while a>=b:
        print("{} ".format(a),end="")
        a=a+1
elif a>b:
    while a<=b:
        print("{} ".format(a),end="")
        b=b+1
else:
    print("異なる値を入力してください")

