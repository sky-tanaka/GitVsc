def show_items(**items):
    for key,value in items.items():
        print("{}:{} ".format(key,value))
    print()

show_items(key1="hoge",key2="fuga")

show_items(k1="Hello",k2="Python",k3="Programming")