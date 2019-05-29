# -*- coding: utf-8 -*-
# Developer : Mengyang Liu
# Date      : 2019-05-16 10:17
# File_Name : exp5.py
# Tool      : PyCharm
import wx
import numpy as np
import re
from sklearn.neighbors import KNeighborsClassifier

class MyPanel(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)
        try:
            image_file = './back.jpg'
            to_bmp_image = wx.Image(image_file, wx.BITMAP_TYPE_ANY).Rescale(700,400).ConvertToBitmap()
            self.bitmap = wx.StaticBitmap(self, -1, to_bmp_image, (0, 0))
            image_width = to_bmp_image.GetWidth()
            image_height = to_bmp_image.GetHeight()
            set_title = '%s %d x %d' % (image_file, 700, 400)
            parent.SetTitle(set_title)
        except IOError:
            raise SystemExit

class GUI(object):

    def __init__(self):
        app = wx.App()
        window = wx.Frame(None, title="订餐系统", size=(700, 400))
        self.panel = MyPanel(window, -1)

        label = wx.StaticText(self.panel, label="Python订餐系统", pos=(250, 20))
        self.button_submit = wx.Button(self.panel, label="submit", pos=(200, 300))
        window.Bind(wx.EVT_BUTTON, self.generate_order, self.button_submit)

        self.menu1 = wx.StaticText(self.panel, label="奥尔良鸡腿堡", pos=(80, 60))
        self.menu2 = wx.StaticText(self.panel, label="香辣牛肉煲", pos=(80, 100))
        self.menu3 = wx.StaticText(self.panel, label="薯条", pos=(80, 140))
        self.menu4 = wx.StaticText(self.panel, label="冰阔落", pos=(80, 180))
        self.menu5 = wx.StaticText(self.panel, label="雪碧", pos=(80, 220))

        bmp = wx.Image("./add.bmp", wx.BITMAP_TYPE_BMP).Rescale(37, 30).ConvertToBitmap()
        bmp1 = wx.Image("./minus.bmp", wx.BITMAP_TYPE_BMP).Rescale(30, 30).ConvertToBitmap()

        add_button1 = wx.BitmapButton(self.panel, -1, bmp, pos=(550, 60))
        add_button2 = wx.BitmapButton(self.panel, -1, bmp, pos=(550, 100))
        add_button3 = wx.BitmapButton(self.panel, -1, bmp, pos=(550, 140))
        add_button4 = wx.BitmapButton(self.panel, -1, bmp, pos=(550, 180))
        add_button5 = wx.BitmapButton(self.panel, -1, bmp, pos=(550, 220))

        minus_button1 = wx.BitmapButton(self.panel, -1, bmp1, pos=(600, 60))
        minus_button2 = wx.BitmapButton(self.panel, -1, bmp1, pos=(600, 100))
        minus_button3 = wx.BitmapButton(self.panel, -1, bmp1, pos=(600, 140))
        minus_button4 = wx.BitmapButton(self.panel, -1, bmp1, pos=(600, 180))
        minus_button5 = wx.BitmapButton(self.panel, -1, bmp1, pos=(600, 220))

        add_button1.Bind(wx.EVT_BUTTON, self.add1)
        add_button2.Bind(wx.EVT_BUTTON, self.add2)
        add_button3.Bind(wx.EVT_BUTTON, self.add3)
        add_button4.Bind(wx.EVT_BUTTON, self.add4)
        add_button5.Bind(wx.EVT_BUTTON, self.add5)

        minus_button1.Bind(wx.EVT_BUTTON, self.minus1)
        minus_button2.Bind(wx.EVT_BUTTON, self.minus2)
        minus_button3.Bind(wx.EVT_BUTTON, self.minus3)
        minus_button4.Bind(wx.EVT_BUTTON, self.minus4)
        minus_button5.Bind(wx.EVT_BUTTON, self.minus5)

        self.num1 = 0
        self.num2 = 0
        self.num3 = 0
        self.num4 = 0
        self.num5 = 0

        self.num_text1 = wx.StaticText(self.panel, label=str(self.num1), pos=(520, 60))
        self.num_text2 = wx.StaticText(self.panel, label=str(self.num1), pos=(520, 100))
        self.num_text3 = wx.StaticText(self.panel, label=str(self.num1), pos=(520, 140))
        self.num_text4 = wx.StaticText(self.panel, label=str(self.num1), pos=(520, 180))
        self.num_text5 = wx.StaticText(self.panel, label=str(self.num1), pos=(520, 220))


        window.Show(True)
        app.MainLoop()

    def add1(self, event):
        self.num1 += 1
        self.num_text1.SetLabel(str(self.num1))
        self.panel.Refresh()

    def add2(self, event):
        self.num2 += 1
        self.num_text2.SetLabel(str(self.num2))
        self.panel.Refresh()

    def add3(self, event):
        self.num3 += 1
        self.num_text3.SetLabel(str(self.num3))
        self.panel.Refresh()

    def add4(self, event):
        self.num4 += 1
        self.num_text4.SetLabel(str(self.num4))
        self.panel.Refresh()

    def add5(self, event):
        self.num5 += 1
        self.num_text5.SetLabel(str(self.num5))
        self.panel.Refresh()

    def minus1(self, event):
        if self.num1 >= 1:
            self.num1 -= 1
            self.num_text1.SetLabel(str(self.num1))
            self.panel.Refresh()

    def minus2(self, event):
        if self.num2 >= 1:
            self.num2 -= 1
            self.num_text2.SetLabel(str(self.num2))
            self.panel.Refresh()

    def minus3(self, event):
        if self.num3 >= 1:
            self.num3 -= 1
            self.num_text3.SetLabel(str(self.num3))
            self.panel.Refresh()

    def minus4(self, event):
        if self.num4 >= 1:
            self.num4 -= 1
            self.num_text4.SetLabel(str(self.num4))
            self.panel.Refresh()

    def minus5(self, event):
        if self.num5 >= 1:
            self.num5 -= 1
            self.num_text5.SetLabel(str(self.num5))
            self.panel.Refresh()

    def generate_order(self, event):
        menus = [self.menu1, self.menu2, self.menu3, self.menu4, self.menu5]
        nums = [self.num1, self.num2, self.num3, self.num4, self.num5]
        order_message = ""
        for menu, num in zip(menus, nums):
            order_message += "{item: <20}{num: >10}".format(item=menu.Label, num=str(num))
            order_message += '\n'
        dlg = wx.MessageDialog(None, order_message, u"您的订单已生成", wx.YES_NO | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            pass
        dlg.Destroy()


def get_int_from_file(file, reshape=None):
    if reshape is None:
        with open(file) as f:
            content = re.split('\n|,', f.read())
            content = content[:-1]
            content = np.array(content, dtype=np.float)
            content = map(abs, content)
            content = list(content)
            content_indexes = [(index, content[index]) for index in range(len(content))]
            content_indexes.sort(key=lambda content_index:content_index[1])
            return content_indexes
    else:
        with open(file) as f:
            content = re.split('\n|,', f.read())
            content = content[:-1]
            content = np.array(content, dtype=np.uint8)
            content = content.reshape((int(len(content)/3304), 3304))
            return content


def get_indexes(sorted_lables, k):
    dims = []
    for i in range(k):
        dims.append(sorted_lables[i][0])
    return dims


def get_lower_data(data, indexes):
    lower_data = data[:, indexes[0]]
    for i in range(1, len(indexes)):
        lower_data = np.vstack((lower_data, data[:, indexes[i]]))
    return lower_data.T




if __name__ == '__main__':
    # NOTE(lmy): Codes below are bout GUI
    # myGUI = GUI()



    # NOTE(lmy): Codes below are about the data analysis
    CEMT_FILE = '/Users/lmy/学习/大三春/Python computation/EXP5/dataanalysis/label/CEMTL_Male.dat'
    MTL_FILE = '/Users/lmy/学习/大三春/Python computation/EXP5/dataanalysis/label/MTL_Male.dat'
    CMTL_FILE = '/Users/lmy/学习/大三春/Python computation/EXP5/dataanalysis/label/CMTL_Male.dat'
    FILES = [CEMT_FILE, MTL_FILE, CMTL_FILE]
    indexes = []
    k = 3000
    for FILE in FILES:
        indexes.append(get_indexes(get_int_from_file(FILE), k))

    # print(DATA[0])

    TRAIN_FILE = '/Users/lmy/学习/大三春/Python computation/EXP5/dataanalysis/train/MTL_Male_train.dat'

    TrainSample = get_int_from_file(TRAIN_FILE, True)

    labels = np.zeros((1000, 1))
    labels[:500] = 0
    labels[500:] = 1
    TestSample = get_int_from_file('/Users/lmy/学习/大三春/Python computation/EXP5/dataanalysis/test/MTL_Male_test.dat',
                                   True)
    print(TrainSample.shape)
    clf = KNeighborsClassifier(4)
    for index in indexes:
        X_data = get_lower_data(TrainSample, index)
        Test = get_lower_data(TestSample, index)
        print(X_data.shape)
        clf.fit(X=X_data, y=labels)
        labels_test = np.zeros((800, 1))
        labels[:400] = 0
        labels[400:] = 1
        # print(clf.score(TestSample, labels_test))
        error_0 = 0
        error_1 = 0
        for i, value in enumerate(list(clf.predict(Test))):
            if i < 400:
                if value == 1:
                    error_0 += 1
            else:
                if value == 0:
                    error_1 += 1

        print('accuracy:%f' % (1 - (error_0 + error_1) / 800))
        print('0 class recall rate: %f' % (1 - error_0 / 400))
        print('1 class recall rate: %f' % (1 - error_1 / 400))
