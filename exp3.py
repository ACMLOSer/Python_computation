# -*- coding: utf-8 -*-
# Developer : Mengyang Liu
# Date      : 2019-04-11 10:09
# File_Name : exp3.py
# Tool      : PyCharm

from collections import Counter
import matplotlib.pyplot as plt
from random import randint
Month31Set = {1, 3, 5, 7, 8, 10, 12}


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
    year = randint(1990, 2005)
    month = randint(1, 12)
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        if month == 2:
            day = randint(1, 29)
        elif month in Month31Set:
            day = randint(1, 31)
        else:
            day = randint(1, 30)
    else:
        if month == 2:
            day = randint(1, 28)
        elif month in Month31Set:
            day = randint(1, 31)
        else:
            day = randint(1, 30)
    birthday = (year, month, day)
    return birthday


# 每次返回一个班级的生日
def class_generator(student_number):
    class_birthday_list = []
    for i in range(student_number):
        class_birthday_list.append(birthday_generator())
    return class_birthday_list


def class_statics(birthday_counter, student_number):
    for i in range(student_number):
        temp_birthday = birthday_generator()
        birthday_counter[temp_birthday] += 1
        if birthday_counter[temp_birthday] >= 2:
            return True


def check_same_birthday(class_birthday_list):
    for birthday in enumerate(class_birthday_list):
        pass


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item  # 返回item
            seen.add(val)
    return seen


def dedupe_dict(_dict):
    tuple_r_dict = lambda _dict: dict(val[::-1] for val in _dict.items())
    return tuple_r_dict(tuple_r_dict(_dict))

def draw_table():
    print('+————+————+')
    for i in range(4):
        print('|    |    |')
    print('+————+————+')
    for i in range(4):
        print('|    |    |')
    print('+————+————+')

def getLength(item):
    return len(item)

def find_longest_shrinkable(file_path):
    f = open(file_path)
    file_content = f.read().split('\n')
    f.close()
    file_content.sort(key=getLength, reverse=True)




if __name__ == '__main__':
    # number_of_student = int(input('Please input the number of class:'))
    # Odd_list = []
    # birthday_Counter = Counter()
    # for number_of_student in range(1, 400):
    #     birthday_duplicate = 0
    #     birthday_Counter.clear()
    #     for i in range(1000):
    #         if class_statics(birthday_counter=birthday_Counter, student_number=number_of_student):
    #             birthday_duplicate += 1
    #     Odd_list.append(birthday_duplicate / 10)
    # print(Odd_list)
    # plt.figure(figsize=(10, 10))
    # plt.plot(range(1, 400), Odd_list)
    # plt.xlabel('Student number')
    # plt.ylabel('Odd of having same birthday in one class')
    # plt.show()
    # print('*' * 30)

    # Random_test_list = [randint(1, 50) for i in range(100)]
    # Random_test_dict = {key: val for key, val in
    #                     [(chr(randint(ord('a'), ord('z'))), randint(5, 30)) for i in range(26)]}
    # filtered_list_result = dedupe(Random_test_list)
    # filtered_dict_result = dedupe_dict(Random_test_dict)
    # print('unfiltered dict:', Random_test_dict)
    # print('filtered dict:', filtered_dict_result)
    # for result in filtered_list_result:
    #     print(result, ' ', end='')
    # print('\n')
    # print('*' * 30)
    # draw_table()

    find_longest_shrinkable('/Users/lmy/Downloads/EXP3/words.txt')
