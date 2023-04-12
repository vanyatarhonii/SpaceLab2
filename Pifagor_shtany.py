# Функція визначення трикутника Піфагора
def pifagor_shtanu(a, b, c):

    # Визначаємо гіпотенузу, як найдовшу сторону і відповідно катети
    if a>b and a>c:
        hipotenuza = a
        katet1 = b
        katet2 = c
    elif b>a and b>c:
        hipotenuza = b
        katet1 = a
        katet2 = c
    else:
        hipotenuza = c
        katet1 = a
        katet2 = b

    # Перевіряємо чи можна утворити трикутни Піфагора за формулою
    # квадрат гіпотенузи дорінює сумі квадратів катетів
    if hipotenuza**2 == katet1**2 + katet2**2:
        result = True
    else:
        result = False
    return result
a = int(input('Введіть довжину сторони а: '))
b = int(input('Введіть довжину сторони b: '))
c = int(input('Введіть довжину сторони c: '))

result = pifagor_shtanu(a, b, c)
print(result)