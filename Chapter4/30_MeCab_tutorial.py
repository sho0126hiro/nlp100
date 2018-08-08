# -*- coding: utf-8 -*-
# https://qiita.com/ekzemplaro/items/c98c7f6698f130b55d53
import sys
import MeCab

mt = MeCab.Tagger("mecabrc")
str_in="特急はくたかで富山に向かいます。それから、金沢に行って、兼六園に行きます。"
res = mt.parseToNode(str_in)

while res:
    #print (res.surface)
    arr = res.feature.split(",")
    if (arr[1] == "固有名詞"):
        print(res.feature)
        print(arr[6])
    res = res.next
