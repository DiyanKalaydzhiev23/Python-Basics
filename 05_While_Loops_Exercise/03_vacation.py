MAX_DAYS_SPENDING = 5

vacation_price = float(input())
balance = float(input())

days_spending = 0
total_days = 0

while days_spending < MAX_DAYS_SPENDING:
    action = input()   # spend or save
    money = float(input())

    total_days += 1

    if action == "spend":
        # balance = balance - money if balance > money else 0
        balance -= money if balance > money else balance  # option 1 balance -= money; option 2 balance -= balance
        days_spending += 1
    else:
        balance += money
        days_spending = 0

        if balance >= vacation_price:
            print(f"You saved the money for {total_days} days.")
            break
else:
    print("You can't save the money.")
    print(total_days)
