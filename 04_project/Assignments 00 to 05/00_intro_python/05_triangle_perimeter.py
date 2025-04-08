# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

def main():
    side1 = float(input("Enter the length of the first side of the triangle: "))

    side2 = float(input("Enter the length of the second side of the triangle: "))

    side3 = float(input("Enter the length of the third side of the triangle: "))

    perimeter = side1 + side2 + side3

    print("The perimeter of the triangle is:", perimeter)

if __name__ == "__main__":
    main()