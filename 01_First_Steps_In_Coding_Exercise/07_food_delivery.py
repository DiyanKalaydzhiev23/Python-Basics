CHICKEN_PRICE = 10.35
FISH_PRICE = 12.40
VEGETARIAN_PRICE = 8.15
DELIVERY_PRICE = 2.50

PERCENT_FOR_DESSERT = 0.20

chicken_menus_count = int(input())
fish_menus_count = int(input())
vegetarian_menus_count = int(input())

menus_price = (
    chicken_menus_count * CHICKEN_PRICE
        +
    fish_menus_count * FISH_PRICE
        +
    vegetarian_menus_count * VEGETARIAN_PRICE
)

dessert_price = menus_price * PERCENT_FOR_DESSERT

total_price = menus_price + dessert_price + DELIVERY_PRICE

print(total_price)
