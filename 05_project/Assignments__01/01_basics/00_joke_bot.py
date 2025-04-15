# Constants
JOKE = "I told my computer I needed a break… now it won’t stop sending me KitKat ads. 😄"
SORRY = "Sorry I only tell jokes"

def main():
    # Asking the user for input
    user_input = input("What do you want?").lower()
    
    # Checking if the user input is "Joke"
    if user_input == "Joke":
        print(JOKE)  # Print the joke
    else:
        print(SORRY)  # Print the sorry message

# This provided line is required at the end of the file to call the main() function.
if __name__ == '__main__':
    main()