# -*- coding: utf-8 -*-
# Developer : Mengyang Liu
# Date      : 2019-04-28 11:25
# File_Name : EXP4_9.py
# Tool      : PyCharm
"""
模拟快餐订餐场景
(1)定义 4 个类:Customer 顾客类，Employee 商户类，Food 食物类 以
及 Lunch 订餐管理。
(2)Lunch 类包含 Customer 和 Employee 实例，具有下单 order 方法，该方
法要求 Customer 实例调用自身的 placeOrder 向 Employee 对象要求下单，并且获
得 Employee 对象调用 takeOrder 生成和返回一个 Food 对象，Food 对象应当包含 了食物名字符串。调用关系如下:
Lunch.order—〉Customer.placeOrder—〉Employee.takeOrder—〉Food
(3)Lunch 类包含 result 方法，要求 Customer 打印所收到的食物订单。
(4)编写交互式界面验证所设计的订餐系统。
"""
import random
import os

class Customer:
    def __init__(self):
        self.id = random.randint(1000000, 9999999)

    def placeOrder(self):
        pass


class Employee:

    def takeOrder(self):
        pass


class Food:

    def __init__(self, name):
        self.name = name


class Lunch:

    def __init__(self, customer: Customer, employee: Employee):
        self.customer = customer
        self.employee = employee
        self.id = random.randint(1000000, 9999999)

    def order(self):
        self.customer.placeOrder()
        self.employee.takeOrder()

    def result(self):
        pass

