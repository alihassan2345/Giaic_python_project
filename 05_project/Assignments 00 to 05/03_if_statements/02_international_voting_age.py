PETURKSBOUIPO_AGE  = 16
STANLAU_AGE  = 25
MAYENGUA_AGE  = 48

user_age = int(input("Enter your age: "))
if user_age >= PETURKSBOUIPO_AGE:
    print("You are eligible to vote in Peturksbouipo.")
else:
    print("You are not eligible to vote in Peturksbouipo.")
if user_age >= STANLAU_AGE:
    print("You are eligible to vote in Stanlau.")
else:
    print("You are not eligible to vote in Stanlau.")
if user_age >= MAYENGUA_AGE:
    print("You are eligible to vote in Mayengua.")
else:
    print("You are not eligible to vote in Mayengua.")

