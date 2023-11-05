from datetime import date, timedelta, datetime
def get_birthdays_per_week(users):
    if not users:
        return {}
    current_date = date.today()  # Отримуємо поточну дату
    weekdays = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday',
    ]
    birthdays_per_week = {day: [] for day in weekdays}
    all_birthday_passed = True  # Змінна для відстеження, чи всі дні народження вже минули у цьому році
    for user in users:
        name = user['name']
        birthday = user['birthday']
        next_birthday = birthday.replace(year=current_date.year)
        if next_birthday < current_date:
            next_birthday = next_birthday.replace(year=current_date.year + 1)
        if current_date <= next_birthday <= current_date + timedelta(days=7):
            all_birthday_passed = False
            day_of_week = next_birthday.weekday()
            day_name = weekdays[day_of_week]
            if day_name in ['Saturday', 'Sunday']:
                day_name = 'Monday'
            birthdays_per_week[day_name].append(name)
    if all_birthday_passed:
        return {}
    return {day: names for day, names in birthdays_per_week.items() if names}
if __name__ == "__main__":
    users = [
        {'name': 'Daryna', 'birthday': date(2023, 10, 16)},
        {'name': 'Melisa', 'birthday': date(2023, 11, 11)},
        {'name': 'Milosh', 'birthday': date(2023, 12, 12)},
        {'name': 'Oleh', 'birthday': date(2023, 11, 6)},
        {'name': 'Volodymyr', 'birthday': date(2023, 11, 8)},
        {'name': 'Max', 'birthday': date(2023, 11, 10)}
    ]
    result = get_birthdays_per_week(users)
    # Виведення результатів
    for day_name, names in result.items():
        print(f'{day_name}: {", ".join(names)}')