deposit = float(input())  # 1000.00
deposit_term_in_months = int(input())  # 1
yearly_percent = float(input()) / 100  # 0.00...100.00 -> 0.00...1.00

sum_deposit = deposit + deposit_term_in_months * ((deposit * yearly_percent) / 12)

print(sum_deposit)
