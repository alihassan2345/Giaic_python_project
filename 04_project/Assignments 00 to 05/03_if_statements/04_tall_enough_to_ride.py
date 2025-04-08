minimum_height = 7
maximum_height = 10

user_height = float(input("Enter your height in feet: "))

if user_height >= minimum_height and user_height <= maximum_height:
    print("You're tall enough to ride!")
else:
    print("You're not tall enough to ride, but maybe next year!")