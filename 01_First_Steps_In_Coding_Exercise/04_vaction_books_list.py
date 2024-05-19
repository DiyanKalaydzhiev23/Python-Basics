pages = int(input())  # 212
pages_for_one_hour = int(input())  # 20
total_days = int(input())  # 2

total_time_needed = pages // pages_for_one_hour  # 212 // 20 => 10
pages_a_day = total_time_needed // total_days  # 10 / 2 => 5

print(pages_a_day)
