time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third

minutes = total_time // 60  # 124 // 60 = 2
seconds = total_time % 60  # 124 % 60 = 4 => 60 * 2 => 120 remainder 4

print(f"{minutes}:{seconds:02d}")

# Solution 2
# print(f"{minutes}:0{seconds}" if seconds < 10 else f"{minutes}:{seconds}")


# Solution 1
# if seconds < 10:
#     print(f"{minutes}:0{seconds}")
# else:
#     print(f"{minutes}:{seconds}")
