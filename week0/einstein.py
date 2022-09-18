# prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer.

m = int(input("Enter the mass in KGs "))
c = int(300000000)
E = m * c * c
print("Energy in Joules = ", E)