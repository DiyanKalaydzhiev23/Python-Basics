ROSE_PRICE = 5
DAHLIA_PRICE = 3.80
TULIP_PRICE = 2.80
NARCISSUS_PRICE = 3
GLADIOLUS_PRICE = 2.50

type_flowers = input()
count_flowers = int(input())
budget = int(input())

total_price = 0

if type_flowers == "Roses":
    total_price = count_flowers * ROSE_PRICE

    if count_flowers > 80:
        total_price *= 0.90  # 10% off

elif type_flowers == "Dahlias":
    total_price = count_flowers * DAHLIA_PRICE

    if count_flowers > 90:
        total_price *= 0.85  # 15% off

elif type_flowers == "Tulips":
    total_price = count_flowers * TULIP_PRICE

    if count_flowers > 80:
        total_price *= 0.85  # 15% off

elif type_flowers == "Narcissus":
    total_price = count_flowers * NARCISSUS_PRICE

    if count_flowers < 120:
        total_price *= 1.15  # 15% up

elif type_flowers == "Gladiolus":
    total_price = count_flowers * GLADIOLUS_PRICE

    if count_flowers < 80:
        total_price *= 1.20  # 20% up

if total_price <= budget:
    print(f"Hey, you have a great garden with {count_flowers} {type_flowers} and {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")
