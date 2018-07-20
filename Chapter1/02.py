# -*- coding: utf-8 -*-
"""
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""
str1="パトカー"
str2="タクシー"
print("{0}+{1}=".format(str1,str2),end="")
for i in range(8):
    if i % 2 is 0 : print(str1[int(i/2)],end="")
    else          : print(str2[int(i/2)],end="")