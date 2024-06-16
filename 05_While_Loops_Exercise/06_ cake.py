total_pieces = int(input()) * int(input())  # 5, 6 => 5 * 6 => 30
pieces_eaten = 0

while total_pieces >= pieces_eaten:
    pieces = input()  # number or STOP; "5"

    if pieces == "STOP":
        print(f"{total_pieces - pieces_eaten} pieces are left.")
        break

    pieces_eaten += int(pieces)  # "5" => 5
else:
    print(f"No more cake left! You need {pieces_eaten - total_pieces} pieces more.")
