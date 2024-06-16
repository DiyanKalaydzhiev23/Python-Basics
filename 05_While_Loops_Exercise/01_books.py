searched_book = input()  # Troy
searched_books_count = 0

while True:
    book = input()  # book_name or No More Books

    if book == searched_book:
        print(f"You checked {searched_books_count} books and found it.")
        break

    if book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {searched_books_count} books.")
        break

    searched_books_count += 1
