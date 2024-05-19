PEN_PRICE = 5.80
MARKER_PRICE = 7.20
DETERGENT_PRICE = 1.20

pens_packs_count = int(input())
marker_packs_count = int(input())
detergent_liters_count = int(input())
percent_discount = int(input()) / 100

price_before_discount = (
        pens_packs_count * PEN_PRICE
            +
        marker_packs_count * MARKER_PRICE
            +
        detergent_liters_count * DETERGENT_PRICE
)
total_price = price_before_discount - price_before_discount * percent_discount

print(total_price)
