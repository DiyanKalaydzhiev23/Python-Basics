length, width, height = int(input()), int(input()), int(input())
percent_filled = float(input()) / 100

volume_in_liters = length * width * height / 1000
volume_in_liters -= volume_in_liters * percent_filled
# volume_in_liters = volume_in_liters - volume_in_liters * percent_filled

print(volume_in_liters)
