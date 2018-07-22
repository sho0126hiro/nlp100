# -*- coding: utf-8 -*-
"""
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""

def Cipher(msg):
    #check=0 : 暗号化 check =1 複合化
    #a:97 z:122
    msg=list(msg)
    for i in range(len(msg)) :
        if ord(msg[i]) >= 97 or ord(msg[i]) <= 122 :
                #英小文字の場合 
                msg[i]=chr(219-ord(msg[i]))
    msg="".join(msg)
    return msg
    
def main():
    message  = u"Hello world"
    message2 = Cipher(message)
    print(message2)
    message3 = Cipher(message2)
    print(message3)

if __name__  == '__main__':
    main()