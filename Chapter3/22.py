# -*- coding: utf-8 -*-
"""
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
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
        #category=re.search(r"Category:(?P<category>.+?)(\||])",data[line])
        category=re.match(r"\[\[Category:(?P<category>.+?)(\|.*|\]\])",data[line])
        #.+? : 1文字以上の最短マッチ >> category groupに代入
        if category :
            print(category.group("category"))

if __name__  == '__main__':
    main()

"""
イギリス
英連邦王国
G8加盟国
欧州連合加盟国
海洋国家
君主国
島国
1801年に設立された州・地域
"""