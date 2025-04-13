# """Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# Prompt the user to enter the first number.

# Read the input and convert it to an integer.

# Prompt the user to enter the second number.

# Read the input and convert it to an integer.

# Calculate the sum of the two numbers.

# Print the total sum with an appropriate message.

# The provided solution demonstrates a working implementation of this problem, where the main() function guides the user through the process of entering two numbers and displays their sum."""


def main():
    user1 = int(input("Enter first number: "))
    user2 = int(input("Enter second number: "))
    print("Sum of two numbers is: ", user1 + user2)

if __name__ == "__main__":
    main()