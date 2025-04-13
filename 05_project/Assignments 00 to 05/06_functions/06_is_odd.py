def even_odd():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd") 

even_odd()

def loop_even_odd():
    for i in range(1, 11):
        if i % 2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")

loop_even_odd()