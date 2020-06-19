t=(0,"January","Februay","March","April","May","June","July","August","September","October","November","December")
a=int(input("月(1~12)を入力:"))
if a>=1 and a<=12:
    print(t[a])
else:
    print("正しい数値を入力してください")