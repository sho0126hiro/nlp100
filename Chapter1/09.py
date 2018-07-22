# -*- coding: utf-8 -*-
"""
09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文
（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
"""

import random

def main():
    msg="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(msg)
    l=msg.split(' ')
    result=[]
    #並び替え
    #print(l)
    for i in range(len(l)) :
        if len(l[i]) > 4 :
            l2=list(l[i]) #各単語をリスト型に変換
            tmp=l2[1:len(l[i])-1]
            random.shuffle(tmp)
            l2[1:len(l[i])-1]=tmp[0:len(l[i])-2]
            #print(l2)  #先頭と末尾以外でランダムに入れ替えたリスト型
            l2="".join(l2)
            result.append(l2)
        else : 
            result.append(l[i])
    #print(result)
    msg2=" ".join(result)
    print(msg2)




if __name__  == '__main__':
    main()