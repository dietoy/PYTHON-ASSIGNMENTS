
fig1 = float(input("Enter first number:"))
operator = (input("Enter an operator (+, -, *, /): "))
fig2 = float(input("Enter second number:"))

if operator == "+":
    result = fig1 + fig2
elif operator == "-":
    result = fig1 - fig2
elif operator == "*":
    result = fig1 * fig2
elif operator == "/":
    result = fig1 / fig2
else:
    print("Invalid operator!")
print("Result:", result)








