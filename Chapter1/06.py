# -*- coding: utf-8 -*-
"""
06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，
XとYの和集合，積集合，差集合を求めよ．
さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""

def ngram(target,n,type):
    #(str,int,str)
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
    str1="paraparaparadise"
    str2="paragraph"

    X = ngram(str1,2,"char")
    Y = ngram(str2,2,"char")

    X_set = set(X)
    Y_set = set(Y)

    print("X = {}".format(X_set))
    print("Y = {}".format(Y_set))

    XorY  = X_set | Y_set
    XandY = X_set & Y_set
    XdifY = X_set - Y_set
    YdifX = Y_set - X_set

    print("X | Y  = {}".format(XorY))
    print("X & Y  = {}".format(XandY))
    print("X - Y  = {}".format(XdifY))
    print("Y - X  = {}".format(YdifX))

    se=set(["se"])
    print(se)
    print(se and Y)
    #<= subset : 部分集合　左辺の要素全てが右辺に含まれているか判定
    if se <= X_set : print("Xにseは含まれています")
    else           : print("Xにseは含まれていません")
    if se <= Y_set : print("Yにseは含まれています")
    else           : print("Yにseは含まれていません")

if __name__  == '__main__':
    main()