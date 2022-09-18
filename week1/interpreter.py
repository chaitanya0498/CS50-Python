#implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value
#formatted to one decimal place. Assume that the user’s input will be formatted as `x y z`, with one space between `x` and `y` and one space between `y` and `z`, wherein:
#* `x` is an integer
#* `y` is `+`, `-`, `*`, or `/`
#* `z` is an integer
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
