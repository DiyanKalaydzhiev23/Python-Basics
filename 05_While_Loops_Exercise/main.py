salary = 1500

while salary > 0:  # for i in range(10) =>
    withdraw = int(input())

    if withdraw == -1:
        break

    salary -= withdraw


print(salary)
