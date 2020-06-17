a=input("文字列を入力してください：")
if len(a)==0:
    print("文章を入力してください")
elif len(a)>=20:
    print("長い文章ですね")
elif len(a)<20 and len(a)>=5:
    print("中くらいの文章ですね")
elif len(a)<5:
    print("短い文章ですね")
