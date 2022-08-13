#prompt user for the arithmetic expression
expression = input("Type your arithmetic expression with a space in between: ")

#split the expression to three characters x, y, z
x, y, z = expression.split(" ")
x = float(x)
z = float(z)

if y == "+":
    answer = x + z
elif y == "-" :
    answer = x - z
elif y == "*" :
    answer = x * z
elif y == "/" :
    answer = x / z

print(float(answer))
