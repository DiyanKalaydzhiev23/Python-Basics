opened_tabs = int(input())
salary = int(input())

for _ in range(opened_tabs):
    tab = input()

    if tab == "Facebook":
        salary -= 150
    elif tab == "Instagram":
        salary -= 100
    elif tab == "Reddit":
        salary -= 50

    if salary <= 0:
        print(f"You have lost your salary.")
        break
else:
    print(salary)
