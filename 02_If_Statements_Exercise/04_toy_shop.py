PUZZLE_PRICE = 2.60
TALKING_DOLLS_PRICE = 3
TEDDY_BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2

vacation_price = float(input())

puzzles_count = int(input())
talking_dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

total_price = (
    puzzles_count * PUZZLE_PRICE +
    talking_dolls_count * TALKING_DOLLS_PRICE +
    teddy_bears_count * TEDDY_BEAR_PRICE +
    minions_count * MINION_PRICE +
    trucks_count * TRUCK_PRICE
)
total_toys_count = (
    puzzles_count +
    talking_dolls_count +
    teddy_bears_count +
    minions_count +
    trucks_count
)

if total_toys_count >= 50:
    total_price *= 0.75  # total_price = total_price - total_price * 0.25

total_price *= 0.90  # total_price -= total_price * 0.10

if total_price >= vacation_price:
    print(f"Yes! {total_price - vacation_price:.2f} lv left.")
else:
    print(f"Not enough money! {vacation_price - total_price:.2f} lv needed.")
