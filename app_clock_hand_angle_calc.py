def app_hand_angle_calc(hour, minute):

    if hour >= 12:
        hour = hour - 12
    else:
        hour = hour

    degree_minute_hand = 6 * minute
    degree_hour_hand = (hour * 30) + (minute * 0.5)

    def degree_between_hand(value_degree_minute_hand, value_degree_hour_hand):
        check1 = all([value_degree_hour_hand == 0, value_degree_minute_hand == 0])
        check2 = any([value_degree_hour_hand == 0, value_degree_minute_hand == 0])
        if check1:
            return 0
        if check2:
            if value_degree_minute_hand == 0:
                return 360 - value_degree_hour_hand
            elif value_degree_hour_hand == 0:
                return 360 - value_degree_minute_hand
        if value_degree_hour_hand < value_degree_minute_hand:
            return value_degree_minute_hand - value_degree_hour_hand
        if value_degree_minute_hand < value_degree_hour_hand:
            return value_degree_hour_hand - value_degree_minute_hand

    def correction(main_func):
        if main_func >= 181:
            return 360 - main_func
        else:
            return main_func

    return correction(degree_between_hand(degree_minute_hand, degree_hour_hand))


if __name__ == '__main__':
    something = app_hand_angle_calc(15, 50)
