nights = int(input()) - 1  # days - 1 => nights
place_type = input()
review = input()  # positive/negative

price = 0

if place_type == "room for one person":
    price = 18

elif place_type == "apartment":
    price = 25

    if nights < 10:
        price *= 0.70
    elif nights <= 15:
        price *= 0.65
    else:
        price *= 0.50

elif place_type == "president apartment":
    price = 35

    if nights < 10:
        price *= 0.90
    elif nights <= 15:
        price *= 0.85
    else:
        price *= 0.80

if review == "positive":
    price *= 1.25
elif review == "negative":
    price *= 0.90

print(f"{price * nights:.2f}")
