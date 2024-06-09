from math import floor

tournaments = int(input())
starting_points = int(input())

won_tournaments = 0
gained_points = 0

for _ in range(tournaments):
    position = input()  # W F SF

    if position == "W":
        gained_points += 2000
        won_tournaments += 1
    elif position == "F":
        gained_points += 1200
    elif position == "SF":
        gained_points += 720

print(f"Final points: {gained_points + starting_points}")
print(f"Average points: {floor(gained_points / tournaments)}")
print(f"{won_tournaments / tournaments * 100:.2f}%")
