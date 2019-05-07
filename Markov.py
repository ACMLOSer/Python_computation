# -*- coding: utf-8 -*-
# Developer : Mengyang Liu
# Date      : 2019-05-07 09:06
# File_Name : Markov.py
# Tool      : PyCharm

from urllib.request import urlopen
from random import randint


class Markov:
    """
    Markov 类用于进行文本分析
    Examples:
        >>> my_markov = Markov()
        >>> my_markov.build_word_dict(text="this is a good example.", n=0)
    """

    def __init__(self):
        self.word_dict = {}

    @staticmethod
    def word_list_sum(word_list):
        sum = 0
        for word, value in word_list.items():
            sum += value
        return sum

    def retrieve_random_word(self, word_list):
        rand_index = randint(1, self.word_list_sum(word_list))
        for word, value in word_list.items():
            rand_index -= value
            if rand_index < 0:
                return word

    @staticmethod
    def merge_to_string(word_list):
        """
        将单词列表合并为字符串
        Args:
            word_list: 单词列表

        Returns:
            返回一个字符串，中间以空格分割单词

        """
        res = ""
        for word in word_list:
            res += word + ' '
        return res

    def build_word_dict(self, text, n):
        """
        分析输入的文本，并返回前缀与后缀
        Args:
            text: 需要分析的原始文本内容
            n: 文本分析的阶数，代表前缀的长度

        Returns:
            字典包含前缀和后缀以及后缀出现的次数

        """
        # 剔除换行符和引号
        text = text.replace("\n", " ")
        text = text.replace("\"", "")
        text = text.replace("--", "")
        text = text.replace("*", "")
        # 保证每个标点符号都和前面的单词在一起
        # 这样不会被剔除，保留在马尔科夫链中
        punctuation = [',', '.', ';', ':', '!', '?']
        for symbol in punctuation:
            text = text.replace(symbol, " " + symbol + " ")
        words = text.split(" ")
        # 过滤空单词
        words = [word for word in words if word != ""]

        word_dict = {}
        for i in range(1, len(words)):
            if i + n < len(words) - 1:
                temp_string = self.merge_to_string(words[i - 1:i + n])
                if temp_string not in word_dict:
                    # 为前缀新建一个字典
                    word_dict[temp_string] = {}
                if words[i + n] not in word_dict[temp_string]:
                    word_dict[temp_string][words[i + n]] = 0
                word_dict[temp_string][words[i + n]
                                       ] = word_dict[temp_string][words[i + n]] + 1
        return word_dict


# text = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
# TEXT = open('./emma.txt').read()
# wordDict = build_word_dict(TEXT, 2)
# print(wordDict['The Project Gutenberg '])
# # 生成链长为100的马尔科夫链
# length = 100
# chain = ""
# currentWord = "I"
# for i in range(0, length):
#     chain += str(currentWord)
#     currentWord = retrieve_random_word(wordDict[currentWord])
# print(chain)
