# -*- coding: utf-8 -*-
"""
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
"""

def ngram(target,n,type):
    result=[]
    if type is "word":
        #単語:N-gram
        for i in range(len(target)-n+1):
            result.append(target[i:i+n])
    if type is "char":
        #文字:N-gram
        list=target.split(' ')
        target=''.join(list)
        for i in range(len(target)-n+1):
            result.append(target[i:i+n])
    return result

def main():
    str="I am an NLPer"
    charbigram=[]
    list=str.split(' ')
    char_ngram=ngram(str,3,"char")
    print(char_ngram)
    word_ngram=ngram(list,3,"word")
    print(word_ngram)

if __name__  == '__main__':
    main()