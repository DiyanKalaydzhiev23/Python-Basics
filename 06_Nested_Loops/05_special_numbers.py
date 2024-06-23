number = int(input())

for n in range(1111, 10_000):
    for digit in str(n):  # 1111 => "1111"
        if digit == "0":
            break
        if number % int(digit) != 0:
            break
    else:
        print(n, end=" ")
