NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
THINNER_PRICE = 5
BAGS_PRICE = 0.40

EXTRA_NYLON = 2
EXTRA_PAINT_PERCENT = 0.10
WORKERS_MATERIALS_PERCENTAGE_SALARY = 0.30

nylon = int(input())
paint = int(input())
thinner = int(input())
work_hours = int(input())

nylon += EXTRA_NYLON  # nylon = nylon + 2
paint += paint * EXTRA_PAINT_PERCENT  # paint = paint + paint * 0.10 || paint = paint * 1.1 || paint *= 1.1

materials_price = (
    nylon * NYLON_PRICE
        +
    paint * PAINT_PRICE
        +
    thinner * THINNER_PRICE
        +
    BAGS_PRICE
)

price_of_work_for_one_hour = materials_price * WORKERS_MATERIALS_PERCENTAGE_SALARY
total_work_price = price_of_work_for_one_hour * work_hours

total_price = materials_price + total_work_price

print(total_price)
