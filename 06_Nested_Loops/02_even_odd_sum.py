num_one, num_two = int(input()), int(input())

for number in range(num_one, num_two + 1):
    even_sum, odd_sum = 0, 0

    for idx, digit in enumerate(str(number)):  # 100001 => "100001"
        if idx % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    if even_sum == odd_sum:
        print(number, end=" ")
