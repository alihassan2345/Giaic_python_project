# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:
def main():
    mass = float(input("Enter mass in kg: "))
    speed_of_light = 3e8
    energy = mass * (speed_of_light ** 2)

    print(f"The equivalent energy of {mass} kg is {energy} Joules.")

if __name__ == "__main__":
    main()
