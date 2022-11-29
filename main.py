print('Выбери')
print('1 - Калькулятор')
print('2 - Конвертер мер и весов')
print('3 - Расчет доходности вклада')
print('4 - Перевод из различных систем счисления в десятичную')

setting = int(input('Выбор: '))

if setting == 1:

    num_1 = int(input('Введи первое число: '))
    num_2 = int(input('Введи второе число: '))

    print('Какую операцию ты хочешь выполнить?')
    print('1 - Сложение')
    print('2 - Вычитание')
    print('3 - Умножение')
    print('4 - Деление')
    print('5 - Вычисление остатка от деления')
    print('6 - Возведение в степень')

    operation = int(input('Выбор: '))

    if operation == 1:  # сложение
        print('Ответ:', num_1 + num_2)

    elif operation == 2:  # вычитание
        print('Ответ:', num_1 - num_2)

    elif operation == 3:  # умножение
        print('Ответ:', num_1 * num_2)

    elif operation == 4:  # деление
        a = int(input('1 - Целочисленное деление\n2 - Деление с остатком\nВыбор: '))
        if a == 1:
            print('Ответ:', num_1 // num_2)
        elif a == 2:
            print('Ответ:', num_1 / num_2)
        else:
            print('Ошибка')

    elif operation == 5:
        print('Ответ:', num_1 % num_2)

    elif operation == 6:
        print('Ответ:', num_1 ** num_2)

    else:
        print('Ошибка')

elif setting == 2:

    print('1 - Конвертер мер')
    print('2 - Конвертер весов')
    select = int(input('Выбор: '))

    if select == 1:
        length = int(input('Какая длина?\nВведите: '))

        print('В каких это единицах измерения?')
        print('1 - Миллиметры')
        print('2 - Сантиметры')
        print('3 - Дециметры')
        print('4 - Метры')
        print('5 - Километры')

        from_unit = int(input('Выбор: '))

        if from_unit == 1:  # миллиметры
            print(length / 10, 'сантиметров')
            print(length / 100, 'дециметров')
            print(length / 1000, 'метров')
            print(length / 1000000, 'километров')

        if from_unit == 2:  # сантиметры
            print(length * 10, 'миллиметров')
            print(length / 10, 'дециметров')
            print(length / 100, 'метров')
            print(length / 100000, 'километров')

        if from_unit == 3:  # дециметры
            print(length * 100, 'миллиметров')
            print(length * 10, 'сантиметров')
            print(length / 10, 'метров')
            print(length / 10000, 'километров')

        if from_unit == 4:  # метры
            print(length * 1000, 'миллиметров')
            print(length * 100, 'сантиметров')
            print(length * 10, 'дециметров')
            print(length / 1000, 'километров')

        if from_unit == 5:  # километры
            print(length * 1000000, 'миллиметров')
            print(length * 100000, 'сантиметров')
            print(length * 10000, 'дециметров')
            print(length * 1000, 'метров')

    elif select == 2:

        weight = int(input('Какой вес?\nВведите: '))

        print('В каких это единицах измерения?')
        print('1 - Граммы')
        print('2 - Килограммы')
        print('3 - Центнеры')
        print('4 - Тонны')

        from_unit = int(input('Выбор: '))

        if from_unit == 1:
            print(weight / 1000, 'килограмм')
            print(weight / 100000, 'центнеров')
            print(weight / 1000000, 'тонн')

        elif from_unit == 2:
            print(weight * 1000, 'грамм')
            print(weight / 100, 'центнеров')
            print(weight / 1000, 'тонн')

        elif from_unit == 3:
            print(weight * 100000, 'грамм')
            print(weight * 100, 'килограмм')
            print(weight / 10, 'тонны')

        elif from_unit == 4:
            print(weight * 1000000, 'грамм')
            print(weight * 1000, 'килограмм')
            print(weight * 10, 'центнеров')

elif setting == 3:

    print('1 - Расчет простых процентов')
    print('2 - Расчет сложных процентов')

    a = int(input('Выберите: '))

    if a == 1:
        deposit_sum = float(input('Сумма вклада: '))
        interest_rate = float(input('Процентная ставка: '))
        deposit_days = int(input('Количество дней вклада: '))
        days_per_year = int(input('Количество дней в году: '))

        percents = (deposit_sum * interest_rate * deposit_days / days_per_year) / 100

        print('Начислено процентов:', round(percents, 1))
        print('Общая сумма:', deposit_sum + round(percents, 1))

    if a == 2:

