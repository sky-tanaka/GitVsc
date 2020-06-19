list1=[n for n in range (1,11) if n%2==0]

print("１から１０までの偶数：{}".format(list1))

list2=[n for n in range(1,11) if 10%n==0]

print("１０の約数：{}".format(list2))