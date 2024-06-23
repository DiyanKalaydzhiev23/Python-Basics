from math import sqrt

sum_prime, sum_non_prime = 0, 0

while True:
    command = input()  # "5"

    if command == "stop":
        break

    current_number = int(command)  # "5" => 5

    if current_number < 0:
        print("Number is negative.")
        continue

    for number in range(2, int(sqrt(current_number)) + 1):
        if current_number % number == 0:
            sum_non_prime += current_number
            break
    else:
        sum_prime += current_number

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
