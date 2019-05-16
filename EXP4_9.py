# -*- coding: utf-8 -*-
# Developer : Mengyang Liu
# Date      : 2019-04-28 11:25
# File_Name : EXP4_9.py
# Tool      : PyCharm

import nltk
import random
file = open('emma.txt', 'r')
walden = file.read()
walden = walden.split()
def makePairs(arr, n):
    pairs = []
    for i in range(len(arr)):
        if i+n+1 < len(arr):
            temp = (arr[i:i+n], arr[i+n])
            pairs.append(temp)
    return pairs


def generate(cfd, word='the', num=1000):
    for i in range(num):
        arr = []  # make an array with the words shown by proper count
        for j in cfd[word]:
            for k in range(cfd[word][j]):
                arr.append(j)

        print(word, end=' ')
        word = arr[int((len(arr)) * random.random())]


pairs = makePairs(walden, 3)
print(pairs)
cfd = nltk.ConditionalFreqDist(pairs)
# generate(cfd)