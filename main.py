# -----------------------------------------------------------
# Проект «Калькулятор» для Кода Будущего
#
# Гондин Тимур
# Email: tim.gondin@gmail.com
# -----------------------------------------------------------
print('Какая программа вам нужна?')
print('1 - Калькулятор')
print('2 - Конвертер мер и весов')
print('3 - Расчет доходности вклада')
print('4 - Перевод из различных систем счисления в десятичную')

setting = int(input('Выбор: '))

if setting == 1:  # если пользователь выбрал "1 - Калькулятор"

    num_1 = int(input('Введите первое число: '))
    num_2 = int(input('Введите второе число: '))

    print('Какую операцию вы хотите выполнить?')
    print('1 - Сложить')
    print('2 - Вычесть')
    print('3 - Умножить')
    print('4 - Поделить')
    print('5 - Вычислить остататок от деления')
    print('6 - Возвести в степень')

    operation = int(input('Выбор: '))

    if operation == 1:  # если пользователь выбрал "1 - Сложить"
        print('Ответ:', num_1 + num_2)

    elif operation == 2:  # если пользователь выбрал "2 - Вычесть"
        print('Ответ:', num_1 - num_2)

    elif operation == 3:  # если пользователь выбрал "3 - Умножить"
        print('Ответ:', num_1 * num_2)

    elif operation == 4:  # если пользователь выбрал "4 - Поделить"
        choice = int(input('1 - Целочисленное деление\n2 - Деление с остатком\nВыбор: '))

        if choice == 1:  # если пользователь выбрал "1 - Целочисленное деление"
            print('Ответ:', num_1 // num_2)

        elif choice == 2:  # если пользователь выбрал "2 - Деление с остатком"
            print('Ответ:', num_1 / num_2)

        else:
            print('Ошибка')  # выводит сообщение об ошибке, если пользователь не выбрал 1 или 2

    elif operation == 5:  # если пользователь выбрал "5 - Вычислить остаток от деления"
        print('Ответ:', num_1 % num_2)

    elif operation == 6:  # если пользователь выбрал "6 - Возвести в степень"
        print('Ответ:', num_1 ** num_2)

    else:
        print('Ошибка')  # выводит сообщение об ошибке, если пользователь не правильно выбрал

elif setting == 2:  # если пользователь в начале выбрал "2 - Конвертер мер и весов"

    print('1 - Конвертер мер')
    print('2 - Конвертер весов')

    select = int(input('Выбор: '))  # спрашивается, запустить конвертер мер или конвертер весов

    if select == 1:  # если пользователь выбрал "1 - Конвертер мер"
        length = int(input('Какая длина?\nВведите: '))  # спрашивает значение

        print('В каких это единицах измерения?')  # спрашивает, в каких единицах измерения это значение
        print('1 - Миллиметры')
        print('2 - Сантиметры')
        print('3 - Дециметры')
        print('4 - Метры')
        print('5 - Километры')

        from_unit = int(input('Выбор: '))  # просит выбрать

        if from_unit == 1:  # если пользователь выбрал "1 - Миллиметры"
            print(length / 10, 'сантиметров')  # переводит введенное значение в другие единицы измерения
            print(length / 100, 'дециметров')
            print(length / 1000, 'метров')
            print(length / 1000000, 'километров')

        elif from_unit == 2:  # если пользователь выбрал "2 - Сантиметры"
            print(length * 10, 'миллиметров')  # переводит введенное значение в другие единицы измерения
            print(length / 10, 'дециметров')
            print(length / 100, 'метров')
            print(length / 100000, 'километров')

        elif from_unit == 3:  # если пользователь выбрал "3 - Дециметры"
            print(length * 100, 'миллиметров')  # переводит введенное значение в другие единицы измерения
            print(length * 10, 'сантиметров')
            print(length / 10, 'метров')
            print(length / 10000, 'километров')

        elif from_unit == 4:  # если пользователь выбрал "4 - Метры"
            print(length * 1000, 'миллиметров')  # переводит введенное значение в другие единицы измерения
            print(length * 100, 'сантиметров')
            print(length * 10, 'дециметров')
            print(length / 1000, 'километров')

        elif from_unit == 5:  # если пользователь выбрал "5 - Километры"
            print(length * 1000000, 'миллиметров')  # переводит введенное значение в другие единицы измерения
            print(length * 100000, 'сантиметров')
            print(length * 10000, 'дециметров')
            print(length * 1000, 'метров')

        else:
            print('Ошибка')  # выводит на экран сообщение об ошибке, если пользователь не правильно выбрал

    elif select == 2:  # если пользователь выбрал "2 - Конвертер весов"
        weight = int(input('Какой вес?\nВведите: '))  # спрашивает значение

        print('В каких это единицах измерения?')  # спрашивает, в каких единицах измерения это значение
        print('1 - Граммы')
        print('2 - Килограммы')
        print('3 - Центнеры')
        print('4 - Тонны')

        from_unit = int(input('Выбор: '))  # просит выбрать

        if from_unit == 1:  # если пользователь выбрал "1 - Граммы"
            print(weight / 1000, 'килограмм')
            print(weight / 100000, 'центнеров')
            print(weight / 1000000, 'тонн')

        elif from_unit == 2:  # если пользователь выбрал "2 - Килограммы"
            print(weight * 1000, 'грамм')
            print(weight / 100, 'центнеров')
            print(weight / 1000, 'тонн')

        elif from_unit == 3:  # если пользователь выбрал "3 - Центнеры"
            print(weight * 100000, 'грамм')
            print(weight * 100, 'килограмм')
            print(weight / 10, 'тонны')

        elif from_unit == 4:  # если пользователь выбрал "4 - Тонны"
            print(weight * 1000000, 'грамм')
            print(weight * 1000, 'килограмм')
            print(weight * 10, 'центнеров')

        else:
            print('Ошибка')  # выводит на экран сообщение об ошибке, если пользователь не правильно выбрал

    else:
        print('Ошибка')  # выводит на экран сообщение об ошибке, если пользователь не правильно выбрал

elif setting == 3:  # если пользователь в начале выбрал "3 - Расчет доходности вклада"
    print('1 - Расчет простых процентов')  # спрашивает, необходимо сделать расчет простых процентов или сложных
    print('2 - Расчет сложных процентов')

    a = int(input('Выберите: '))  # просит выбрать

    if a == 1:  # если пользователь выбрал "1 - Расчет простых процентов"
        deposit_sum = float(input('Сумма вклада: '))  # просит ввести необходимые для расчетов значение
        interest_rate = float(input('Процентная ставка: '))
        deposit_days = int(input('Количество дней вклада: '))

        percents = (deposit_sum * interest_rate * deposit_days / 365) / 100  # формула для расчета

        print('Начислено процентов:', round(percents, 1))  # выводит на экран ответ
        print('Общая сумма:', deposit_sum + round(percents, 1))

    if a == 2:  # если пользователь выбрал "2 - Расчет сложных процентов"
        print('1 - Ежедневная капитализация')  # спрашивает, какова периодичность капитализации
        print('2 - Ежемесячная капитализация')
        print('3 - Ежеквартальная капитализация')

        select = int(input())  # просит выбрать

        if select == 1:  # если пользователь выбрал "1 - Ежедневная капитализация"
            deposit_sum = float(input('Сумма вклада: '))  # просит ввести необходимые для расчетов значение
            interest_rate = float(input('Процентная ставка: '))
            investment_period_days = int(input('Срок вложения в днях: '))

            interest_rate = interest_rate / 100  # конвертирует значение процентной ставки в десятичную дробь

            result = deposit_sum * ((1 + (interest_rate / 365)) ** investment_period_days)  # формула для расчета
            percents = result - deposit_sum  # вычисляет прибыль

            print('Начислено процентов:', round(percents, 1))  # выводит на экран ответ
            print('Общая сумма:', round(result, 1))

        elif select == 2:  # если пользователь выбрал "2 - Ежемесячная капитализация"
            deposit_sum = float(input('Сумма вклада: '))  # просит ввести необходимые для расчетов значение
            interest_rate = float(input('Процентная ставка: '))
            investment_period_months = int(input('Срок договора в месяцах: '))

            interest_rate = interest_rate / 100  # конвертирует значение процентной ставки в десятичную дробь

            result = deposit_sum * ((1 + (interest_rate / 12)) ** investment_period_months)  # формула для расчета
            percents = result - deposit_sum  # вычисляет прибыль

            print('Начислено процентов:', round(percents, 1))  # выводит на экран ответ
            print('Общая сумма:', round(result, 1))

        elif select == 3:  # если пользователь выбрал "3 - Ежеквартальная капитализация"
            deposit_sum = float(input('Сумма вклада: '))  # просит ввести необходимые для расчетов значение
            interest_rate = float(input('Процентная ставка: '))
            investment_period_quarters = int(input('Срок договора в кварталах: '))

            interest_rate = interest_rate / 100  # конвертирует значение процентной ставки в десятичную дробь

            result = deposit_sum * ((1 + (interest_rate / 4)) ** investment_period_quarters)  # формула для расчета
            percents = result - deposit_sum  # вычисляет прибыль

            print('Начислено процентов:', round(percents, 1))  # выводит на экран ответ
            print('Общая сумма:', round(result, 1))

        else:
            print('Ошибка')  # выводит на экран сообщение об ошибке, если пользователь не правильно выбрал

    else:
        print('Ошибка')  # выводит на экран сообщение об ошибке, если пользователь не правильно выбрал

elif setting == 4:  # если пользователь в начале выбрал "4 - Перевод из различных систем счисление в десятичную"
    print('Из какой системы счисления нужно перевести?')
    print('1 - Двоичная')
    print('2 - Восьмеричная')
    print('3 - Шестнадцатиричная')

    a = int(input('Выберите: '))  # просит сделать выбор

    if a == 1:  # если пользователь выбрал "1 - Двоичная"
        num = (input('Введите число: '))  # просит ввести числовое значение
        num = int(num, 2)  # переводит введенное числовое значение из двоичной в десятичную систему

        print('Результат:', num)  # выводит на экран результат перевода

    if a == 2:  # если пользователь выбрал "2 - Восьмеричная"
        num = (input('Введите число: '))  # просит ввести число
        num = int(num, 8)  # переводит введенное число из восьмеричной в десятичную систему

        print('Результат:', num)  # выводит на экран результат перевода

    if a == 3:  # если пользователь выбрал "3 - Шестнадцатиричная"
        num = (input('Введите число: '))  # просит ввести число
        num = int(num, 16)  # переводит введенное число из шестнадцатиричной в десятичную систему

        print('Результат:', num)  # выводит на экран результат перевода
    else:
        print('Ошибка')  # выводит на экран сообщение об ошибке, если пользователь не правильно выбрал

else:
    print('Ошибка')  # выводит на экран сообщение об ошибке, если пользователь не правильно выбрал
