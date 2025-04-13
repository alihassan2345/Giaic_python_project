# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.

def main():
    anthon = 21
    beth = anthon + 6
    chenn = beth + 20
    drew = chenn + anthon
    ethan = chenn

    print(f"Anton is {anthon} years old")
    print(f"Beth is {beth} years old")
    print(f"Chen is {chenn} years old")
    print(f"Drew is {drew} years old")
    print(f"Ethan is {ethan} years old")

if __name__ == "__main__":
    main()
