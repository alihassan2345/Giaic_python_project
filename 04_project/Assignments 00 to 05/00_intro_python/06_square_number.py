# Ask the user for a number and print its square (the product of the number times itself).

def main():
    user_square = int(input("Enter a number: "))
    user_final = user_square * user_square
    print(f"your number is {user_square} and the square of your number is {user_final}")

if __name__ == "__main__":
    main()