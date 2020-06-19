def show_loop(str,num):
    if(num<=0):
        print("繰り返し回数は正の数で入れてください")
        return
    i=0
    while i<num:
        print("{} ".format(str),end="")
        i=i+1
    print()

show_loop("Hello",3)
show_loop("World",4)
show_loop("Python",-1)