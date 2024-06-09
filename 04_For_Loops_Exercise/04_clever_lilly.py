MONEY_INCREASE = 10
BROTHER_TAX = 1

years = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money_given = MONEY_INCREASE  # 10 20 30 40
money_from_gifts = 0
money_from_toys = 0

for age in range(1, years + 1):
    if age % 2 == 0:
        money_from_gifts += money_given - BROTHER_TAX
        money_given += MONEY_INCREASE
    else:
         money_from_toys += toy_price

total_money = money_from_gifts + money_from_toys

if total_money >= washing_machine_price:
    print(f"Yes! {total_money - washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price - total_money:.2f}")
