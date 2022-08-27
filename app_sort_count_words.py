import string


def count_sort_words(any_text):
    # Удалить знаки переноса строк, которые в Python пишется как '\n' и '\r'
    any_text = any_text.replace('\n', ' ')
    # Удалить знаки переноса строк, которые в Python пишется как '\n' и '\r'
    any_text = any_text.replace('\r', ' ')

    punctuation = ['.', ',', ';', ':', '!', '?', '"',
                       "'", '(', ')', '...', '—', '«', '»', '.', ' - ']
    # punctuation = string.punctuation

    # посчитаем знаки препинания
    def count_punctuation(some_string: str) -> str:
        count_punct = 0
        for value in some_string:
            if value in punctuation:
                count_punct = count_punct + 1
        return count_punct

    sum_punctuation = count_punctuation(any_text)

    # Удалим знаки препинания
    def marks_remove(some_string: str) -> str:  
        return "".join(elements for elements in some_string if elements not in punctuation)

    # создадим новую строку уже без знаков препинания и сделаем все слова строчными
    new_text = marks_remove(any_text)
    new_text = new_text.lower()

    # split - метод, который разбивает сроку и делает из нее новый список
    mas = new_text.split(' ')
    for x in mas:  # лишние пробелы превратились в '', удалим их:
        if '' in mas:
            mas.remove('')

    # set - метод создания множества. Мы превращаем список в множество. Множества не содержат дублей.
    unique = set(mas)

    # создадим и заполним словарь, ключ - это слово, значение - число повторений слова в списке.
    raw_dic = {}
    for word in unique:
        raw_dic[word] = int(mas.count(word))

    sorted_dict = {}  # создадим новый словарь
    ''' Сортировка:  Тут с помощью параметра "key" - указываем как именно осуществлять сортировку
    И мы сортируем по значениям (метод .get возвращает значение ключа). Тоесть, значение - у нас кол-во слов,
    по нему и сортируем.  reverse - перевернуть'''
    sorted_keys = sorted(raw_dic, key=raw_dic.get, reverse=True)

    # заполним новый словарь: ключ - отсортированные ключи = значение (число) по ключу из первого словаря.
    for k in sorted_keys:
        sorted_dict[k] = raw_dic[k]

    list_one_word = []  # это под список слов, повторяющихся один раз.
    dic_for_return = {}
    for key, value in sorted_dict.items():
        if value > 1:
            #print(f'Слово "{key}" : повторений: {value}')
            dic_for_return[key] = value
        if value == 1:
            list_one_word.append(key)  # добавим в цикле в список
    list_one_word = ", ".join(list_one_word)

    # bild like a json)
    new_list = []

    for key, value in dic_for_return.items():
        new_dic = {}
        new_dic['word'] = key
        new_dic['sum'] = value
        new_list.append(new_dic)


    json_return = {'sum_all_words': len(mas),
                   'sum_unique_words': len(unique),
                   'sum_punctuation' : sum_punctuation,
                   'list_one_word': list_one_word,
                  # 'dic_for_return': dic_for_return,
                   'new_list': new_list
                   }
    return json_return


if __name__ == "__main__":
    print(count_sort_words('This is the house that Jack built. This is the malt that lay in the house that Jack built. This is the rat that ate the malt That lay in the house that Jack built.'))
    print()
