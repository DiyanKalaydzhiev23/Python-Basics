EXTRAS_NEEDED_FOR_DISCOUNT = 150

budget = float(input())
extras = int(input())
clothing_price = float(input())

decor = budget * 0.10  # 1000 * 0.10 => decor = 100

if extras > EXTRAS_NEEDED_FOR_DISCOUNT:
    clothing_price *= 0.90  # 10% off

total_price = decor + clothing_price * extras

if total_price > budget:
    print("Not enough money!")
    print(f"Wingard needs {total_price - budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget - total_price:.2f} leva left.")
