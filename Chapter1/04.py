# -*- coding: utf-8 -*-
"""
04. 元素記号
"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
という文を単語に分解し，
1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
それ以外の単語は先頭の2文字を取り出し，
取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
"""
str="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
length=[]
dict={}
x=[1,5,6,7,8,9,15,16,19]
str=str.replace('.',"") #delete '.'
list=str.split(' ')

y=0
for i in range(len(list)):
    for j in range(len(x)):
        if i is x[j]-1 : 
            dict.update({list[i][0]:i+1})
            y=1
    if y is 0 : dict.update({list[i][0:2]:i+1})
    y=0

print(dict)