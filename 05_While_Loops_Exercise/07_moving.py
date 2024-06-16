total_space = int(input()) * int(input()) * int(input())  # w * h * l
space_filled = 0

while space_filled < total_space:
    box = input()

    if box == "Done":
        print(f"{total_space - space_filled} Cubic meters left.")
        break

    space_filled += int(box)
else:
    print(f"No more free space! You need {space_filled - total_space} Cubic meters more.")
