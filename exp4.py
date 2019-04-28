# -*- coding: utf-8 -*-
# Developer : Mengyang Liu
# Date      : 2019-04-28 10:22
# File_Name : exp4.py
# Tool      : PyCharm

"""
编写拥有
a、对象成员 hour，minute 和 second 的时间类 Time;
b、重载 __str__和__add__方法;
c、方法 time2int:把时间对象转换为秒数;
d、方法 printtime:输出时间;
e、方法 isafter:判断两个时间对象的先后;
f、方法 increment: 计算对象经过 n〉0 秒后时间;
g、方法 isvalid:判断时间对象合法性。
在主函数 设计代码验证 Time 各个方法的正确性。
"""


class Time:

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '{} {} {}'.format(self.hour, self.minute, self.minute)

    def __add__(self, other):
        temp = Time()
        temp.hour = self.hour + other.hour
        temp.minute = self.minute + other.minute
        temp.second = self.second + other.second
        temp.minute += temp.second // 60
        temp.hour += temp.minute // 60
        temp.hour %= 24
        temp.minute %= 60
        temp.second %= 60
        return temp

    def printtime(self):
        print('Current time: {} hour {} minutes {} second'.format(
              self.hour, self.minute, self.second))

    def isvalid(self):
        if 0 <= self.hour < 24 and 0 <= self.minute < 60 and 0 <= self.second < 60:
            return True
        else:
            return False

    @staticmethod
    def isafter(time1, time2):
        if time1.hour > time2.hour:
            return True
        elif time1.hour < time2.hour:
            return False
        else:
            if time1.minute > time2.minute:
                return True
            elif time1.minute < time2.minute:
                return False
            else:
                if time1.second > time2.second:
                    return True
                elif time1.second < time2.second:
                    return False
                else:
                    return False

    @staticmethod
    def time2int(time):
        return time.hour * 3600 + time.minute * 60 + time.second

    def increment(self, n):
        temp = Time(n // 3600, (n % 3600) // 60, (n % 60))
        return self + temp


if __name__ == '__main__':
    test_time1 = Time(23, 56, 44)
    test_time2 = Time(21, 4, 24)
    print(Time.isafter(test_time1, test_time2))
    print(Time.time2int(test_time1))
    added_time = test_time1 + test_time2
    added_time.printtime()
    print(test_time1.isvalid())
    print(Time(56, 56, 111).isvalid())
    Time(23, 56, 4).increment(3600).printtime()
    print(str(test_time1))
