my_list = []

n = int(input("how many items do you want to add in the list? "))

for i in range(n):
     item = input(f"Enter your Item {i+1} ")
     my_list.append(item)
     
   

print("Final list:", my_list)
