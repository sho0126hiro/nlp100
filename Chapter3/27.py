# -*- coding: utf-8 -*-
"""
27. 内部リンクの除去
26の処理に加えて，テンプレートの値からMediaWikiの
内部リンクマークアップを除去し，テキストに変換せよ
（参考: マークアップ早見表）．
マークアップ早見表：https://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8

[[記事名]]	
[[記事名|表示文字]]	 
[[記事名#節名|表示文字]]
|がある場合、表示文字を取得
#memo
    問題の意図が、内部リンク自体を削除するか、内部リンクマークアップ([[ | ]])
    を削除するか不明だったため、後者のプログラムを作製している。

"""
import gzip
import json
import re
import pprint #pretty print

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
    #UK_data : str
    #re.DOTALL : 改行にもマッチさせる
    m=re.search(r"{{基礎情報\s国(?P<info>.+?)\n}}",UK_data,re.DOTALL)
    if m :
        info = m.group("info")
    #m.group("info"):基礎情報が入ってる
    info_list=info.split('\n|')
    info_dict={}
    sortlist=[]
    for i in range(len(info_list)): 
        #マークアップ除去
        info_list[i]=re.sub(r"\'{2,4}","",info_list[i])
        info_list[i]=re.sub(r"\[\[(.+?)\]\]",lambda m : m.group(1).split('|')[-1],info_list[i])
        #上のようにすれば1行で書ける
        #m.group(1) : (.+?)を取得し、|で分割後、[-1]で一番最後の要素（表示文字）を取得
        info_list[i]=re.sub(r"\|"," ",info_list[i])
        m2=re.split(r"\s+=\s+",info_list[i])
        #re.split : "\s+=\s+"で区切ってm2リストに格納する
        if len(m2) == 2 :
            info_dict[m2[0]]=m2[1]
            sortlist.append(m2[0])
    #出現順にソートして表示
    info=sorted(info_dict.items(),key=lambda m2 : sortlist.index(m2[0]))
    #info_dict.items() ; 辞書のタプル型リストを取得
    pprint.pprint(info)

if __name__  == '__main__':
    main()

"""
[('略名', 'イギリス'),
 ('日本語国名', 'グレートブリテン及び北アイルランド連合王国'),
 ('公式国名',
  '{{lang en United Kingdom of Great Britain and Northern '
  'Ireland}}<ref>英語以外での正式国名:<br/>\n'
  '*{{lang gd An Rìoghachd Aonaichte na Breatainn Mhòr agus Eirinn mu '
  'Thuath}}（スコットランド・ゲール語）<br/>\n'
  '*{{lang cy Teyrnas Gyfunol Prydain Fawr a Gogledd Iwerddon}}（ウェールズ語）<br/>\n'
  '*{{lang ga Ríocht Aontaithe na Breataine Móire agus Tuaisceart na '
  'hÉireann}}（アイルランド語）<br/>\n'
  '*{{lang kw An Rywvaneth Unys a Vreten Veur hag Iwerdhon '
  'Glédh}}（コーンウォール語）<br/>\n'
  '*{{lang sco Unitit Kinrick o Great Breetain an Northren '
  'Ireland}}（スコットランド語）<br/>\n'
  '**{{lang sco Claught Kängrick o Docht Brätain an Norlin Airlann}}、{{lang '
  'sco Unitet Kängdom o Great Brittain an Norlin '
  'Airlann}}（アルスター・スコットランド語）</ref>'),
 ('国旗画像', 'Flag of the United Kingdom.svg'),
 ('国章画像', 'ファイル:Royal Coat of Arms of the United Kingdom.svg 85px イギリスの国章'),
 ('国章リンク', '（イギリスの国章 国章）'),
 ('標語', '{{lang fr Dieu et mon droit}}<br/>（フランス語:神と私の権利）'),
 ('国歌', '女王陛下万歳 神よ女王陛下を守り給え'),
 ('位置画像', 'Location_UK_EU_Europe_001.svg'),
 ('公用語', '英語（事実上）'),
 ('首都', 'ロンドン'),
 ('最大都市', 'ロンドン'),
 ('元首等肩書', 'イギリスの君主 女王'),
 ('元首等氏名', 'エリザベス2世'),
 ('首相等肩書', 'イギリスの首相 首相'),
 ('首相等氏名', 'デーヴィッド・キャメロン'),
 ('面積順位', '76'),
 ('面積大きさ', '1 E11'),
 ('面積値', '244,820'),
 ('水面積率', '1.3%'),
 ('人口統計年', '2011'),
 ('人口順位', '22'),
 ('人口大きさ', '1 E7'),
 ('人口値',
  '63,181,775<ref>[http://esa.un.org/unpd/wpp/Excel-Data/population.htm United '
  'Nations Department of Economic and Social Affairs>Population '
  'Division>Data>Population>Total Population]</ref>'),
 ('人口密度値', '246'),
 ('GDP統計年元', '2012'),
 ('GDP値元',
  '1兆5478億<ref '
  'name="imf-statistics-gdp">[http://www.imf.org/external/pubs/ft/weo/2012/02/weodata/weorept.aspx?pr.x=70&pr.y=13&sy=2010&ey=2012&scsm=1&ssd=1&sort=country&ds=.&br=1&c=112&s=NGDP%2CNGDPD%2CPPPGDP%2CPPPPC&grp=0&a= '
  'IMF>Data and Statistics>World Economic Outlook Databases>By '
  'Countrise>United Kingdom]</ref>'),
 ('GDP統計年MER', '2012'),
 ('GDP順位MER', '5'),
 ('GDP値MER', '2兆4337億<ref name="imf-statistics-gdp" />'),
 ('GDP統計年', '2012'),
 ('GDP順位', '6'),
 ('GDP値', '2兆3162億<ref name="imf-statistics-gdp" />'),
 ('GDP/人', '36,727<ref name="imf-statistics-gdp" />'),
 ('建国形態', '建国'),
 ('確立形態1', 'イングランド王国／スコットランド王国<br />（両国とも連合法 (1707年) 1707年連合法まで）'),
 ('確立年月日1', '927年／843年'),
 ('確立形態2', 'グレートブリテン王国建国<br />（連合法 (1707年) 1707年連合法）'),
 ('確立年月日2', '1707年'),
 ('確立形態3', 'グレートブリテン及びアイルランド連合王国建国<br />（連合法 (1800年) 1800年連合法）'),
 ('確立年月日3', '1801年'),
 ('確立形態4', '現在の国号「グレートブリテン及び北アイルランド連合王国」に変更'),
 ('確立年月日4', '1927年'),
 ('通貨', 'スターリング・ポンド UKポンド (&pound;)'),
 ('通貨コード', 'GBP'),
 ('時間帯', '±0'),
 ('夏時間', '+1'),
 ('ISO 3166-1', 'GB / GBR'),
 ('ccTLD', '.uk / .gb<ref>使用は.ukに比べ圧倒的少数。</ref>'),
 ('国際電話番号', '44'),
 ('注記', '<references />')]
"""