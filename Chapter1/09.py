# -*- coding: utf-8 -*-
"""
09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文
（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
"""

import random

def replace(char):
    # cher length : 2
    char=list(char)
    tmp=char[0]
    char[0]=char[1]
    char[1]=tmp
    char="".join(char)
    return char

def main():
    msg="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    l=msg.split(' ')
    result=[]
    for i in range(len(l)) :
        #各単語の先頭と末尾の文字以外を消す
        if len(l[i]) > 2 :
            result.append(l[i][0]+l[i][len(l[i])-1])
        else : 
            result.append(l[i]) 
    print(result)
    #並び替え
    for i in range(len(l)) : 
        if len(l[i]) > 4 : 
            if random.randrange(2) : result[i]=replace(result[i])
    print(result)

if __name__  == '__main__':
    main()