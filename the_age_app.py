def the_age_app(name, age):
    if 5 <= age <= 20:
        return f'Привет {name} !!! Тебе уже {age} лет!!!'
    else:
        a = str(age)  # ввожу переменную a, которая равна age в виде сроки
        last_digit = int(a[-1])  # эту комбинацию подсмотрел, Получить последний символ строки и преобразовать его в число.

        if last_digit == 2 or last_digit == 3 or last_digit == 4:
            return f'Привет {name} !!! Тебе уже {age} года!!!'
        elif last_digit == 1:  # elif пришется тогда, когда после первого if больше не выполнять второй блок.
            return f'Привет {name} !!! Тебе уже {age} год!!!'
        else:
            return f'Привет {name} !!! Тебе уже {age} лет!!!'