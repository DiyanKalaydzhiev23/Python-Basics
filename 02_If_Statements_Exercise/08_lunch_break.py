from math import ceil

series_name = input()  # Suits
episode_length = int(input())  # 35
break_length = int(input())  # 60

lunch_time = break_length / 8  # 7.5
leisure_time = break_length / 4  # 15

time_needed = leisure_time + lunch_time + episode_length  # 7.5 + 15 + 35 => 57.5
time_left = break_length - time_needed  # 60 - 57.5 => 2.5

if time_left >= 0:
    print(f"You have enough time to watch {series_name} and left with {ceil(time_left)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(abs(time_left))} more minutes.")
