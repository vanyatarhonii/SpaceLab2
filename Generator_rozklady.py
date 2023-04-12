import datetime

# Функція, що генерує розклад робочих днів працівника
def work_generator(days, work_days, rest_days, start_date):
    List = []   # Список робочих днів, які треба повернути
    one_day = datetime.timedelta(days=1)
    i = 0       # Рахуємо дні
    j = 1       # Рахуємо дні з циклу робочі + вихідні і по колу

    while (i < days):                               # Проходимо всі дні
        if j <= work_days:                          # якщо робочі
            List.append(start_date + one_day * i)   # Додаємо до списку робочих днів, щоб повернути
        elif j == work_days+rest_days:              # Перевіряємо чи пройшли цикл робочі + вихідні
            j = 0                                   # Перезапускаємо цикл робочих днів
        else:
            pass
        j = j + 1
        i = i + 1
    return List


days = 5
work_days = 2
rest_days = 1
start_date = datetime.datetime(2020, 1, 30)
result = work_generator(days, work_days, rest_days, start_date)
print(result)
