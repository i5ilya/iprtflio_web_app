import string


def count_sort_words(any_text):
    # Удалить знаки переноса строк, которые в Python пишется как '\n' и '\r'
    any_text = any_text.replace("\r", " ").replace("\n", " ")

    punctuation = string.punctuation  # возьмем знаки препинания из библиотеки string

    # Посчитаем знаки препинания
    def count_punctuation(some_string: str) -> int:
        count = 0
        for value in some_string:
            if value in punctuation:
                count += 1
        return count

    sum_punctuation = count_punctuation(any_text)

    # Удалим знаки препинания
    def marks_remove(some_string: str) -> str:
        return "".join(elements for elements in some_string if elements not in punctuation)

    # создадим новую строку уже без знаков препинания и сделаем все слова строчными
    new_text = marks_remove(any_text)
    new_text = new_text.lower()

    # split - метод, который разбивает сроку и делает из нее новый список
    mas1 = new_text.split(' ')
    # for x in mas:  # лишние пробелы превратились в '', удалим их:
    mas = [value for value in mas1 if value != '']

    # set - метод создания множества. Мы превращаем список в множество. Множества не содержат дублей.
    unique = set(mas)

    # создадим и заполним словарь, ключ - это слово, значение - число повторений слова в списке.
    raw_dic = {word : int(mas.count(word)) for word in unique}
    # for word in unique:
    #     raw_dic[word] = int(mas.count(word))


    ''' Сортировка:  Тут с помощью параметра "key" - указываем как именно осуществлять сортировку
    И мы сортируем по значениям (метод .get возвращает значение ключа). То есть, значение - у нас кол-во слов,
    по нему и сортируем.  reverse - перевернуть'''
    sorted_keys = sorted(raw_dic, key=raw_dic.get, reverse=True)

    # заполним новый словарь: ключ - отсортированные ключи = значение (число) по ключу из первого словаря.
    sorted_dict = {k: raw_dic[k] for k in sorted_keys}  # создадим новый словарь
    # for k in sorted_keys:
    #     sorted_dict[k] = raw_dic[k]

    list_one_word = []  # это под список слов, повторяющихся один раз.
    dic_for_return = {}  # конечный словарь
    for key, value in sorted_dict.items():
        if value > 1:
            # print(f'Слово "{key}" : повторений: {value}')
            dic_for_return[key] = value
        if value == 1:
            list_one_word.append(key)  # добавим в цикле в список

    list_one_word.sort()
    list_one_word = ", ".join(list_one_word)

    # bild like a json data
    new_list = []
    for key, value in dic_for_return.items():
        new_dic = {}
        new_dic['word'] = key
        new_dic['sum'] = value
        new_list.append(new_dic)

    json_return = {'sum_all_words': len(mas),
                   'sum_unique_words': len(unique),
                   'sum_punctuation': sum_punctuation,
                   'list_one_word': list_one_word,
                   'new_list': new_list
                   }
    return json_return


if __name__ == "__main__":
    print(count_sort_words(
        'This is the house that Jack built. This is the malt that lay in the house that Jack built. This is the rat that ate the malt That lay in the house that Jack built.'))
    print()
