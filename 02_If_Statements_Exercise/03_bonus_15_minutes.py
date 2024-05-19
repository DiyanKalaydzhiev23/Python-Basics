# Solution 1
# BONUS_MINUTES = 15
#
# hours = int(input())  # 23
# minutes = int(input())  # 59
#
# minutes += BONUS_MINUTES  # 74
#
# if minutes > 59:
#     hours += 1  # 23 -> 24
#     minutes -= 60  # 74 - 60 -> 14
# if hours > 23:
#     hours -= 24  # 24 - 24 => 0
#
# print(f"{hours}:{minutes:02d}")

# Solution 2
BONUS_MINUTES = 15

hours = int(input())  # 23
minutes = int(input())  # 59

total_minutes = hours * 60 + minutes + BONUS_MINUTES  # 1454

new_hours = total_minutes // 60 % 24  # 24 % 24 => 0
new_minutes = total_minutes % 60

print(f"{new_hours}:{new_minutes:02d}")
