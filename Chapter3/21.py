# -*- coding: utf-8 -*-
"""
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
カテゴリ名を宣言している行:[[Category:.*]]
Wiki help : https://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8
regex : https://www.sejuku.net/blog/23232
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
    #print(data)
    for line in range(len(data)):
        Category=re.findall(r'\[\[Category:.*\]\]',data[line])
        if Category :
            print(data[line])
    
if __name__  == '__main__':
    main()

"""
[[Category:イギリス|
[[Category:英連邦王国|
[[Category:G8加盟国]
[[Category:欧州連合加盟国]
[[Category:海洋国家]
[[Category:君主国]
[[Category:島国|
[[Category:1801年に設立された州・地域]
"""