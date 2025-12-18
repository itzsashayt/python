def create_calendar(month, year, days):
    print(f"calendar: {month} {year}")

    current_day = 1

    while current_day <= days:
        week = []
        for _ in range(7):
            if current_day <= days:
                week.append(str(current_day))
                current_day += 1
            else:
                break

        print(" ".join(week))

create_calendar('Randomner', 2045, 23)