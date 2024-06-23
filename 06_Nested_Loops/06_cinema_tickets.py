total_students, total_standard, total_kids = 0, 0, 0

while True:
    movie_name = input()

    if movie_name == "Finish":
        break

    capacity = int(input())
    sold_tickets = 0

    while sold_tickets < capacity:
        type_ticket = input()  # student, standard, kid, End

        if type_ticket == "End":
            break

        if type_ticket == "student":
            total_students += 1
        elif type_ticket == "standard":
            total_standard += 1
        elif type_ticket == "kid":
            total_kids += 1

        sold_tickets += 1

    print(f"{movie_name} - {sold_tickets / capacity * 100:.2f}% full.")

total_tickets = total_students + total_standard + total_kids

print(f"Total tickets: {total_tickets}")
print(f"{total_students / total_tickets * 100:.2f}% student tickets.")
print(f"{total_standard / total_tickets * 100:.2f}% standard tickets.")
print(f"{total_kids / total_tickets * 100:.2f}% kids tickets.")
