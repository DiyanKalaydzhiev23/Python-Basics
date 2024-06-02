SPRING_PRICE = 3000
SUMMER_AND_AUTUMN_PRICE = 4200
WINTER_PRICE = 2600

FIRST_DISCOUNT_LEVEL = 0.10
SECOND_DISCOUNT_LEVEL = 0.15
THIRD_DISCOUNT_LEVEL = 0.25
EVEN_COUNT_DISCOUNT = 0.05

budget = int(input())
season = input()
count_people = int(input())

total_price = 0

if season == "Spring":
    total_price = SPRING_PRICE
elif season == "Winter":
    total_price = WINTER_PRICE
else:
    total_price = SUMMER_AND_AUTUMN_PRICE

if count_people <= 6:
    total_price *= (1 - FIRST_DISCOUNT_LEVEL)  # 1 - 0.10 => 0.90 => 90% from price => 10% off
elif 7 <= count_people <= 11:
    total_price *= (1 - SECOND_DISCOUNT_LEVEL)
else:
    total_price *= (1 - THIRD_DISCOUNT_LEVEL)

if season != "Autumn" and count_people % 2 == 0:
    total_price *= (1 - EVEN_COUNT_DISCOUNT)

if total_price <= budget:
    print(f"Yes! You have {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva.")
