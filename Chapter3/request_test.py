#http://requests-docs-ja.readthedocs.io/en/latest/user/quickstart/#url
# -*- coding: utf-8 -*-

import codecs
import json
import re
import gzip
from pprint import pprint


def extract_text(text):
    #gzip file open >> json
    with gzip.open("jawiki-country.json.gz","rt") as f:
        for line in f:
            obj = json.loads(line)
            #type(obj) : class 'dict
            if obj["title"] == text :
                return obj["text"]
                
def extract_base_info(text):
    m = re.search("{{基礎情報[^|]+\|(?P<info_body>.+?)\n}}", text, re.DOTALL)
    if not m:
        return {}

    info_body = m.group("info_body")

    info_dict = {}

    for item in info_body.split("\n|"):
        [key, word] = re.split(r"\s+=\s+", item, maxsplit=1)

        word = remove_section_header(word)
        word = remove_emphasis(word)
        word = remove_category_links(word)
        word = remove_internal_links(word)
        word = remove_external_links(word)
        word = remove_template(word)
        word = remove_unordered_list(word)
        word = remove_define_list(word)
        word = remove_redirect(word)
        word = remove_comment(word)

        info_dict[key] = word

    return info_dict

def remove_section_header(text):
    """見出しのマークアップを除去"""
    return re.sub(r"(=+)(.+?)\1", lambda m: m.group(2), text)

def remove_emphasis(text):
    """強調マークアップを除去"""
    return re.sub(r"'{2,}", "", text)

def remove_category_links(text):
    """カテゴリリンクのマークアップを除去"""
    return re.sub(r"\[\[Category:(.+?)\]\]", lambda m: m.group(1).split("|")[0], text)

def remove_internal_links(text):
    """内部リンクのマークアップを除去"""
    return re.sub(r"\[\[([^]]+)\]\]", lambda m: m.group(1).split("|")[-1], text)

def remove_external_links(text):
    """外部リンクのマークアップを除去"""
    return re.sub(r"\[([^]]+)\]", lambda m: m.group(1).split(" ")[-1], text)

def remove_template(text):
    """スタブのマークアップを除去"""
    return re.sub(r"\{\{(.+?)\}\}", lambda m: m.group(1).split("|")[-1], text)

def remove_unordered_list(text):
    """箇条書きのマークアップを除去"""
    return re.sub(r"^\*+\s*", "", text, flags=re.MULTILINE)

def remove_ordered_list(text):
    """番号付箇条書きのマークアップを除去"""
    return re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)

def remove_define_list(text):
    """定義の箇条書きのマークアップを除去"""
    return re.sub(r"^(:|;)\s*", "", text, flags=re.MULTILINE)

def remove_redirect(text):
    """リダイレクトのマークアップを除去"""
    return re.sub(r"#REDIRECT \[\[(.+?)\]\]", lambda m: m.group(1), text)

def remove_comment(text):
    """コメントアウトのマークアップを除去"""
    return re.sub(r"<!--.*?-->", "", text)


text=extract_text('イギリス')
base_info = extract_base_info(text)


from urllib.parse import urlencode
from urllib import request

flag_image_name = base_info["国旗画像"]
query = urlencode({
    "action": "query",
    "titles": "File:{0}".format(flag_image_name),
    "prop": "imageinfo",
    "iiprop": "url",
    "format": "json",
})
url = "https://commons.wikimedia.org/w/api.php?{0}".format(query)

with request.urlopen(url) as response:
    body = response.read()
    data = json.loads(body.decode("utf-8"))

    pprint(data, indent=4)
    # =>
    # {
    #     'continue': {'continue': '||', 'iistart': '2007-09-03T09:51:34Z'},
    #     'query': {
    #         'pages': {
    #             '347935': {
    #                 'imageinfo': [{
    #                     'descriptionshorturl': 'https://commons.wikimedia.org/w/index.php?curid=347935',
    #                     'descriptionurl': 'https://commons.wikimedia.org/wiki/File:Flag_of_the_United_Kingdom.svg',
    #                     'url': 'https://upload.wikimedia.org/wikipedia/commons/a/ae/Flag_of_the_United_Kingdom.svg'
    #                 }],
    #                 'imagerepository': 'local',
    #                 'ns': 6,
    #                 'pageid': 347935,
    #                 'title': 'File:Flag of the United ''Kingdom.svg'
    #             }
    #         }
    #     }
    # }

    flag_image_url = list(data["query"]["pages"].values())[0]["imageinfo"][0]["url"]

    print(flag_image_url)