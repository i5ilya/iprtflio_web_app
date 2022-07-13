

def ideal_weght(user_height: int, user_sex: str, user_hand: int, user_age: int) -> str:

    # Считаем коэффициент, в функцию будем передаем рост пользователя - height
    def calc_factor(height: int) -> int:
        if height <= 165:
            return 100
        if 166 <= height <= 174:
            return 105
        if height >= 175:
            return 110

    factor = calc_factor(user_height)

    # У нас есть 3 типа телосложения. Их нужно определить и ввести.

    # В функцию передаем пол -sex и длину запястья -hand
    def calc_body_type(sex: str, hand: int) -> str:
        if sex == 'ж' and hand <= 15 or sex == 'м' and hand <= 17:
            return 'small'
        elif sex == 'ж' and 16 <= hand <= 18 or sex == 'м' and 17 < hand <= 20:
            return 'normal'
        else:
            return 'big'

    body_type = calc_body_type(user_sex, user_hand)

    def h_minus_f():  # height minus factor function
        return user_height - factor

    if 20 <= user_age <= 30:
        if body_type == "small":
            # вычли 20% т.к. вес -10% и тонкость кости -10%
            ves = h_minus_f() - (h_minus_f() * 0.2)
            return f'У Вас астенический (тонкокостный) тип телосложения, расчетный вес равен: {round(ves)} кг'
        elif body_type == "normal":
            # вычли 10%, т.к. действует условие возраст
            ves = (h_minus_f()) - ((h_minus_f()) * 0.1)
            return f'У Вас нормостенический (нормокостный) тип телосложения, расчетный вес равен: {round(ves)} кг'
        elif body_type == "big":
            # не вычитали % , т.к. за возраст должны вычесть 10%, а за ширококстность прибавить.
            ves = h_minus_f()
            return f'У Вас гиперстенический (ширококостный) тип телосложения, расчетный вес равен: {round(ves)} кг'
    if 31 <= user_age <= 49:
        if body_type == "small":
            ves = h_minus_f() - (h_minus_f() * 0.1)  # вычли 10% за тонкость кости
            return f'У Вас астенический (тонкокостный) тип телосложения, расчетный вес равен: {round(ves)} кг'
        elif body_type == "normal":
            # нет условий возраст и нет тонкости кости или толстости кости.
            ves = h_minus_f()
            return f'У Вас нормостенический (нормокостный) тип телосложения, расчетный вес равен: {round(ves)} кг'
        elif body_type == "big":
            ves = h_minus_f() + (h_minus_f() * 0.1)  # прибавили 10% за толстость кости
            return f'У Вас гиперстенический (ширококостный) тип телосложения, расчетный вес равен: {round(ves)} кг'
    if user_age >= 50:
        if body_type == "small":
            # вычли 10% за тонкость кости и прибавили 0.6 за возраст
            ves = h_minus_f() - (h_minus_f() * 0.04)
            return f'У Вас астенический (тонкокостный) тип телосложения, расчетный вес равен: {round(ves)} кг'
        elif body_type == "normal":
            ves = h_minus_f() + (h_minus_f() * 0.06)  # прибавили 6% за возраст
            return f'У Вас нормостенический (нормокостный) тип телосложения, расчетный вес равен: {round(ves)} кг'
        elif body_type == "big":
            # прибавили 10% за толстость кости и 6 за возраст
            ves = h_minus_f() + (h_minus_f() * 0.16)
            return f'У Вас гиперстенический (ширококостный) тип телосложения, расчетный вес равен: {round(ves)} кг'


if __name__ == '__main__':
    #print(ideal_weght(168, 'м', 15, 96))
    number = 20
    while number <= 100:
        number += 1
        print(f"возраст {number: } {ideal_weght(180, 'м', 18, number)}")