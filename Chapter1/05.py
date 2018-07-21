# -*- coding: utf-8 -*-
"""
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
"""

def ngram(target,n,type):
    #(list,int,str)
    result=[]
    list=target.split(' ')
    if type is "word":
        #単語:N-gram
        for i in range(len(list)-n+1):
            result.append(list[i:i+n])
    if type is "char":
        #文字:N-gram
        target=''.join(list)
        for i in range(len(target)-n+1):
            result.append(target[i:i+n])
    return result

def main():
    str="I am an NLPer"
    word_ngram=ngram(str,2,"word")
    print(word_ngram)
    char_ngram=ngram(str,2,"char")
    print(char_ngram)

if __name__  == '__main__':
    main()