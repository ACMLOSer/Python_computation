# -*- coding: utf-8 -*-
# Developer : Mengyang Liu
# Date      : 2019-05-16 10:17
# File_Name : exp5.py
# Tool      : PyCharm
import wx
class GUI(object):

    def __init__(self):
        app = wx.App()
        window = wx.Frame(None, title="wxPython 你好！", size=(600, 400))
        panel = wx.Panel(window)
        label = wx.StaticText(panel, label="Hello World", pos=(300, 200))
        window.Show(True)
        app.MainLoop()


if __name__ == '__main__':
    mygui = GUI()
