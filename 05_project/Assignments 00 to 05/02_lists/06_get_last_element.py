# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

list = []

n = int(input("how many items do you want to add in the list? "))

for i in range(n):
    item = input(f"Enter your Item {i+1} ")
    list.append(item)

print("Your list is: ", list)
print("The first element of the list is: ", list[-1])