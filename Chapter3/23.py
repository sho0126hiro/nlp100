# -*- coding: utf-8 -*-
"""
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．

style manual       : https://ja.wikipedia.org/wiki/Wikipedia:%E3%82%B9%E3%82%BF%E3%82%A4%E3%83%AB%E3%83%9E%E3%83%8B%E3%83%A5%E3%82%A2%E3%83%AB
mark up quick help : https://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8

==text==      : level2 : 1
===text===    : level3 : 2
====text====  : level4 : 3
=====text==== : level5 : 4
"""
import gzip
import json
import re

def extract_text(text):
    #gzip file open >> json
    with gzip.open("jawiki-country.json.gz","rt") as f:
        for line in f:
            obj = json.loads(line)
            #type(obj) : class 'dict
            if obj["title"] == text :
                return obj["text"]
def main():
    UK_data=extract_text('イギリス')
    data=UK_data.split('\n')
    for line in range(len(data)):
        m=re.search(r"(?P<level>==+)(\s*)(?P<section>.+?)(\s*)=+",data[line])
        #re.match : 先頭　re.serch　:文字列全体の中
        if m :
            print(m.group("section"),end=" ")
            level=m.group("level")
            print(len(level)-1)

if __name__  == '__main__':
    main()

"""
国名 1
歴史 1
地理 1
気候 2
政治 1
外交と軍事 1
地方行政区分 1
主要都市 2
科学技術 1
経済 1
鉱業 2
農業 2
貿易 2
通貨 2
企業 2
交通 1
道路 2
鉄道 2
海運 2
航空 2
通信 1
国民 1
言語 2
宗教 2
婚姻 2
教育 2
文化 1
食文化 2
文学 2
哲学 2
音楽 2
イギリスのポピュラー音楽 3
映画 2
コメディ 2
国花 2
世界遺産 2
祝祭日 2
スポーツ 1
サッカー 2
競馬 2
モータースポーツ 2
脚注 1
関連項目 1
外部リンク 1
"""