def min_2(x,y):
    if x<y:
        r=x
    else:
        r=y
    return r

a=input("1つ目の整数:")
b=input("2つ目の整数:")

print("最小値は{}です。".format(min_2(a,b)))