a=int(input("西暦を入力："))
if a>=0:
    if a%4==0 and a%100!=0 or a%400==0:
        print("閏年")
    else:
        print("閏年ではない")
else:
    print("不適切な値です")
    

