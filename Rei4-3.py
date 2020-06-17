n=0
while True:
    s=input("正の数を入力：")
    if not s.isdecimal():
        continue
    n=int(s)
    if n>0:
        break
print("入力された数：{}".format(n))