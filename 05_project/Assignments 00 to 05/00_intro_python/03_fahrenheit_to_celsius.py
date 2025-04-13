# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.
def main():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"your fahrenheit tempreature {fahrenheit} converted in celsius is {celsius}")

if __name__ == "__main__":
    main()