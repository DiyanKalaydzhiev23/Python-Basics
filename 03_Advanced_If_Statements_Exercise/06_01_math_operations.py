num1 = int(input())
num2 = int(input())
operator = input()

result = None

if operator == "+" or operator == "-" or operator == "*":
    math_result = eval(f'{num1} {operator} {num2}')
    result = f"{num1} {operator} {num2} = {math_result} "
    result += ("- even" if math_result % 2 == 0 else "- odd")
elif num2 == 0:
    result = f"Cannot divide {num1} by zero"
elif operator == "/":
    result = f"{num1} / {num2} = {num1 / num2:.2f}"
elif operator == "%":
    result = f"{num1} % {num2} = {num1 % num2}"

print(result)
