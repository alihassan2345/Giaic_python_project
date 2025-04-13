# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.

list = []

n = int(input("how many items do you want to add in the list? "))

for i in range(n):


    item = input(f"Enter your Item {i+1} ")
    list.append(item)

print("Your list is: ", list)
print("The first element of the list is: ", list[0])