yearly_fee = int(input())  # 1000

shoes = yearly_fee - yearly_fee * 0.40  # yearly_fee * 0.60
clothes = shoes - shoes * 0.20  # shoes * 0.80
ball = clothes / 4
accessories = ball / 5

total_sum = yearly_fee + shoes + clothes + ball + accessories

print(total_sum)
