PREMIERE_TICKET = 12
NORMAL_TICKET = 7.50
DISCOUNT_TICKET = 5

type_movie = input()
rows, cols = int(input()), int(input())

income = 0
cinema_capacity = rows * cols

if type_movie == "Premiere":
    income = cinema_capacity * PREMIERE_TICKET
elif type_movie == "Normal":
    income = cinema_capacity * NORMAL_TICKET
elif type_movie == "Discount":
    income = cinema_capacity * DISCOUNT_TICKET

print(f"{income:.2f} leva")
