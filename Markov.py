# -*- coding: utf-8 -*-
# Developer : Mengyang Liu
# Date      : 2019-05-07 09:06
# File_Name : Markov.py
# Tool      : PyCharm

from random import randint, choice
import random


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
        res += word + " "
    return res[:-1]


class Markov:
    """
    Markov 类用于进行文本分析
    Examples:
    '''
        my_markov = Markov()
        my_markov.generate_words_dict(text="this is a good example.", n=0)
        print(my_markov.word_dict)
    '''
    """

    def __init__(self):
        self.word_dict = {}
        self.n = 0
        self.word_pair = None

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
                # print(word)
                return word

    def generate_words_dict(self, text, n):
        """
        分析输入的文本，并返回前缀与后缀.构建n阶马尔可夫词典
        Args:
            text: 需要分析的原始文本内容
            n: 文本分析的阶数，代表前缀的长度

        Returns:
            字典包含前缀和后缀以及后缀出现的次数

        """
        # 剔除换行符和引号等特殊符号
        self.n = n + 1
        text = text.replace("\n", " ")
        text = text.replace("\"", " ")
        text = text.replace("--", " ")
        text = text.replace("*", " ")
        text = text.replace("'", "")
        text = text.replace('`', "")
        text = text.replace("(", " ")
        text = text.replace(")", " ")
        text = text.replace("_", " ")
        text = text.replace("[", " ")
        text = text.replace("]", " ")
        # 保证每个标点符号都和前面的单词在一起
        punctuation = [',', '.', ';', ':', '!', '?']
        for symbol in punctuation:
            text = text.replace(symbol, " " + symbol + " ")
        words = text.split(" ")
        # 过滤空单词
        words = [word for word in words if word != ""]
        self.word_pair = make_pairs(words, n)


def make_pairs(arr, n):
    pairs = []
    for i in range(len(arr)):
        if i + n + 1 < len(arr):
            temp = (arr[i:i + n], arr[i + n])
            pairs.append(temp)
    return pairs


def pair2dict_list(pairs):
    word_dict = {}
    for pair in pairs:
        cur_key = merge_to_string(pair[0])
        if cur_key not in word_dict:
            word_dict[cur_key] = []
        word_dict[cur_key].append(pair[1])
    # print(word_dict)
    return word_dict


def pair2dict_tuple(pairs):
    word_dict = {}
    for pair in pairs:
        cur_key = merge_to_string(pair[0])
        if cur_key not in word_dict:
            word_dict[cur_key] = []
        word_dict[cur_key].append(pair[1])
    for key in word_dict.keys():
        word_dict[key] = tuple(word_dict[key])
    # print(word_dict)
    return word_dict


def pair2dict(pairs):
    word_dict = {}
    for pair in pairs:
        cur_key = merge_to_string(pair[0])
        if cur_key not in word_dict:
            word_dict[cur_key] = {}
        if pair[1] not in word_dict[cur_key]:
            word_dict[cur_key][pair[1]] = 1
        else:
            word_dict[cur_key][pair[1]] += 1
    return word_dict


def select_word(word_dict):
    if type(word_dict) == dict:
        while True:
            for word, value in word_dict.items():
                if random.random() * value > 0.9:
                    return word
    elif type(word_dict) == list:
        return choice(word_dict)
    elif type(word_dict) == tuple:
        return random.choice(word_dict)


def create_key(current_sentence, n):
    return merge_to_string(current_sentence.split(' ')[-n:])


def generate_sentence(file_path, level: int, sentence_num: int):
    """
    Args:
        file_path: 训练文件路径
        level: 整型
        sentence_num: 生成句子个数

    Returns:

    """
    markov = Markov()
    text = open(file_path).read()
    markov.generate_words_dict(text, level)

    word_dict1 = pair2dict_list(markov.word_pair)
    word_dict2 = pair2dict(markov.word_pair)
    word_dict3 = pair2dict_tuple(markov.word_pair)
    # print(word_dict.items())
    print('*'*40)
    for word_dict, name in [(word_dict1, 'list'), (word_dict2, 'dict'), (word_dict3, 'tuple')]:
        import time
        start_time = time.time()
        while True:
            start = choice(list(word_dict.keys()))
            if start[0].isupper():
                break
        current_sentence = start
        key = start
        tmp_sentence_num = sentence_num
        while tmp_sentence_num > 0:
            cur_word = select_word(word_dict[key])
            current_sentence += ' ' + cur_word
            if cur_word == '.':
                tmp_sentence_num -= 1
            key = create_key(current_sentence, level)
        print(name + ' Using time:', time.time() - start_time)
    print('*' * 40 + '\n\n\n')
    return current_sentence



if __name__ == '__main__':
    FILE_PATH1 = './emma.txt'
    FILE_PATH2 = './whitefang.txt'
    generated_string = generate_sentence(FILE_PATH2, 2, 300)
    # print(generated_string)
    for sentence in generated_string.split('.'):
        print(sentence + '.')
