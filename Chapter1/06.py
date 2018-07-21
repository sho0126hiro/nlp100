# -*- coding: utf-8 -*-
"""
06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，
XとYの和集合，積集合，差集合を求めよ．
さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
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
    str1="paraparaparadise"
    str2="paragraph"
    charbigram=[]
    X=ngram(str1,2,"char")
    Y=ngram(str2,2,"char")
    print(char_ngram)

if __name__  == '__main__':
    main()