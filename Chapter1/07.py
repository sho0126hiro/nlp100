# -*- coding: utf-8 -*-
"""
07. テンプレートによる文生成
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
"""

def Sentence_Generation(x,y,z):
    if type(x) != str : x=str(x)
    if type(y) != str : y=str(y)
    if type(z) != str : z=str(z)
    result = x + 'の時の' + y + 'は' + z
    return result
    
def main():
    x=12
    y="気温"
    z=22.4
    print(Sentence_Generation(x,y,z))


if __name__  == '__main__':
    main()