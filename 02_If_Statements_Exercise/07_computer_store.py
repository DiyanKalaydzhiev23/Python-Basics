GRAPHIC_CARD_PRICE = 250

PROCESSORS_PERCENTAGE_OF_GRAPHIC_CARDS = 0.35
MEMORY_PERCENTAGE_OF_GRAPHIC_CARDS = 0.10

budget = float(input())

graphic_cards_count = int(input())
processors_count = int(input())
memory_count = int(input())

graphic_cards_price = graphic_cards_count * GRAPHIC_CARD_PRICE
processors_price = processors_count * graphic_cards_price * PROCESSORS_PERCENTAGE_OF_GRAPHIC_CARDS
memory_price = memory_count * graphic_cards_price * MEMORY_PERCENTAGE_OF_GRAPHIC_CARDS

total_price = graphic_cards_price + processors_price + memory_price

if graphic_cards_count > processors_count:
    total_price -= total_price * 0.15  # total_price *= 0.85

if total_price <= budget:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")
