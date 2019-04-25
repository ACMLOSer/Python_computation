# -*- coding: utf-8 -*-
# Developer : Mengyang Liu
# Date      : 2019-04-11 10:09
# File_Name : exp3.py
# Tool      : PyCharm

from collections import Counter
import matplotlib.pyplot as plt
from random import randint
from functools import wraps
import time
MONTH31SET = {1, 3, 5, 7, 8, 10, 12}


def practice(fun_c, flag=0):
    print('@' * 30 + str(flag) + '@' * 30)
    @wraps(fun_c)
    def inner(*args, **kwargs):
        result = fun_c(*args, **kwargs)
        if result is not None:
            return result
        else:
            pass
    return inner



def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, n)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))


# 每次返回一个生日
def birthday_generator():
    from random import randint
    # 生成随机的年份和月
    year = randint(1990, 2005)
    month = randint(1, 12)
    # 闰年判断
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        if month == 2:
            day = randint(1, 29)
        elif month in MONTH31SET:
            day = randint(1, 31)
        else:
            day = randint(1, 30)
    else:
        if month == 2:
            day = randint(1, 28)
        elif month in MONTH31SET:
            day = randint(1, 31)
        else:
            day = randint(1, 30)
    # 构造生日元组并返回
    birthday = (year, month, day)
    return birthday


# 每次返回一个班级的生日，此处并不使用，可以用于生成数据进行可视化分析
def class_generator(student_number: int):
    class_birthday_list = []
    for i in range(student_number):
        class_birthday_list.append(birthday_generator())
    return class_birthday_list


# 每次生成一个生日并判断是否已有重复生日出现
def class_statics(birthday_counter: Counter, student_number: int):
    for i in range(student_number):
        temp_birthday = birthday_generator()
        birthday_counter[temp_birthday] += 1
        if birthday_counter[temp_birthday] >= 2:
            return True



def classes_statics():
    start = time.time()
    # number_of_student = int(input('Please input the number of class:'))
    odd_list = []
    birthday_counter = Counter()
    for number_of_student in range(1, 400):
        birthday_duplicate = 0
        birthday_counter.clear()
        for i in range(1000):
            if class_statics(
                    birthday_counter=birthday_counter,
                    student_number=number_of_student):
                birthday_duplicate += 1
        odd_list.append(birthday_duplicate / 10)
    print(odd_list)
    plt.figure(figsize=(10, 10))
    plt.plot(range(1, 400), odd_list)
    plt.xlabel('Student number')
    plt.ylabel('Odd of having same birthday in one class')
    plt.show()
    print(time.time() - start)



def dedupe(items: list, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item  # 返回item
            seen.add(val)



def dedupe_dict(_dict: dict):
    def tuple_r_dict(_dict): return dict(val[::-1] for val in _dict.items())
    return tuple_r_dict(tuple_r_dict(_dict))


def draw_table():
    print('+————+————+')
    for i in range(4):
        print('|    |    |')
    print('+————+————+')
    for i in range(4):
        print('|    |    |')
    print('+————+————+')


def get_length(item: str):
    return len(item)


def find_longest_shrinkable(file_path: str):
    start = time.time()
    with open(file_path) as f:
        file_content = f.read().split('\n')
    file_content.sort(key=get_length, reverse=True)
    temp_words_set = set(file_content)
    for word in file_content:
        # temp_file_content.remove(word)
        if recursive_find(word=word, words_set=temp_words_set):
            print('Find Word:', word)
            break
    print(time.time() - start, find_longest_shrinkable.__name__)


def recursive_find(word: str, words_set: set):
    if word == 'a' or word == 'i':
        return True
    if word not in words_set:
        return False
    else:
        for i in range(len(word)):
            if recursive_find(word[0:i] + word[i + 1:], words_set):
                print(word[0:i] + word[i + 1:] + ' <- ', end='')
                return True
        return False


def list_dict_filter():
    start = time.time()
    random_test_list = [randint(1, 50) for i in range(100)]
    random_test_dict = {
        key: val for key, val in [
            (chr(
                randint(
                    ord('a'), ord('z'))), randint(
                5, 30)) for i in range(26)]}
    filtered_list_result = dedupe(random_test_list)
    filtered_dict_result = dedupe_dict(random_test_dict)
    print('unfiltered dict:', random_test_dict)
    print('filtered dict:', filtered_dict_result)
    print('disposed items in dict:', [item for item in random_test_dict if item in
          random_test_dict and item not in filtered_dict_result])
    for result in filtered_list_result:
        print(result, ' ', end='')
    print('\n')
    print(time.time() - start, list_dict_filter.__name__)


if __name__ == '__main__':
    classes_statics()
    list_dict_filter()
    draw_table()
    find_longest_shrinkable(
        '/Users/lmy/学习/大三春/Python computation/EXP3/words.txt')
