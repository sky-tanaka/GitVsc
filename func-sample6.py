def show_items(*items):
    for i,item in enumerate(items):
        print("{}:{}".format(i,item),end="")
    print()
show_items("ONE","TWO","THREE","FOUR")
show_items("いち","に","さん")
