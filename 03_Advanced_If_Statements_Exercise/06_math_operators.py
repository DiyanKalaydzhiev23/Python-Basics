num1 = int(input())
num2 = int(input())
operator = input()

result = None

if operator == "+":
    result = f"{num1} + {num2} = {num1 + num2} " + ("- even" if (num1 + num2) % 2 == 0 else "- odd")
elif operator == "-":
    result = f"{num1} - {num2} = {num1 - num2} " + ("- even" if (num1 - num2) % 2 == 0 else "- odd")
elif operator == "*":
    result = f"{num1} * {num2} = {num1 * num2} " + ("- even" if (num1 * num2) % 2 == 0 else "- odd")
elif num2 == 0:
    result = f"Cannot divide {num1} by zero"
elif operator == "/":
    result = f"{num1} / {num2} = {num1 / num2:.2f}"
elif operator == "%":
    result = f"{num1} % {num2} = {num1 % num2}"

print(result)
