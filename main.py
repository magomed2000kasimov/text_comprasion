import random
import requests
import string


def text_random_char(length):
    res = ''
    for i in range(0, length):
        res += random.choice(string.ascii_letters)
    return res


def text_random_word(length):
    # ссылка на множество английских слов
    url1 = 'https://svnweb.freebsd.org/csrg/share/dict/words/?view=co'
    tmp = requests.get(url1).text
    tmp = tmp.split()
    res = ''
    while len(res) < length:
        res += random.choice(tmp)
    return res[:length]


def task1():
    # ссылка на Великого Гэтсби
    url1 = 'https://www.gutenberg.org/files/64317/64317-0.txt'
    # ссылка на Приключения Тома Сойера
    url2 = 'https://www.gutenberg.org/files/74/74-0.txt'
    text1 = requests.get(url1).text
    text2 = requests.get(url2).text
    count = 0
    for c1, c2 in zip(text1, text2):
        if c1 == c2:
            count += 1
    print('Длина текстов:', min(len(text1), len(text2)))
    coef = count / min(len(text1), len(text2))
    print('Коэффициент совпадения:', coef)


def task2():
    # ссылка на Великого Гэтсби
    url1 = 'https://www.gutenberg.org/files/64317/64317-0.txt'
    text1 = requests.get(url1).text
    text2 = text_random_char(len(text1))
    count = 0
    for c1, c2 in zip(text1, text2):
        if c1 == c2:
            count += 1
    print('Длина текстов:', min(len(text1), len(text2)))
    coef = count / min(len(text1), len(text2))
    print('Коэффициент совпадения:', coef)


def task3():
    # ссылка на Великого Гэтсби
    url1 = 'https://www.gutenberg.org/files/64317/64317-0.txt'
    text1 = requests.get(url1).text
    text2 = text_random_word(len(text1))
    count = 0
    for c1, c2 in zip(text1, text2):
        if c1 == c2:
            count += 1
    print('Длина текстов:', min(len(text1), len(text2)))
    coef = count / min(len(text1), len(text2))
    print('Коэффициент совпадения:', coef)


def task4():
    text1 = text_random_char(306258)
    text2 = text_random_char(306258)
    count = 0
    for c1, c2 in zip(text1, text2):
        if c1 == c2:
            count += 1
    print('Длина текстов:', min(len(text1), len(text2)))
    coef = count / min(len(text1), len(text2))
    print('Коэффициент совпадения:', coef)


def task5():
    text1 = text_random_word(306258)
    text2 = text_random_word(306258)
    count = 0
    for c1, c2 in zip(text1, text2):
        if c1 == c2:
            count += 1
    print('Длина текстов:', min(len(text1), len(text2)))
    coef = count / min(len(text1), len(text2))
    print('Коэффициент совпадения:', coef)


task1()
task2()
task3()
task4()
task5()
