age=int(input("年齢："))

if 0<=age and age<20:
    print("未成年")
elif age>=20:
    g=input("男性(ｍ)　or　女性(ｆ)")
    if g=="m":
        print("成人男性")
    elif g=="f":
        print("成人女性")
    else:
        print("性別不明")
else:
    print("不適切な値です")
