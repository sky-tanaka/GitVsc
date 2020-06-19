def min_3(x,y,z):
    if x<y and x<z:
        r=x
    elif y>x and y>z:
        r=y
    else:
        r=z
    return r

a=input("1つ目の整数:")
b=input("2つ目の整数:")
c=input("3つ目の整数:")

print("最小値は{}です。".format(min_3(a,b,c)))