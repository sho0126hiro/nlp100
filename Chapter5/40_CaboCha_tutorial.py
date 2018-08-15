# -*- coding: utf-8 -*-
import CaboCha

def main():
    text='太郎はこの本を次郎を見た女性に渡した。'
    c = CaboCha.Parser()
    print('1:parseToString')
    print(c.parseToString(text))
    tree=c.parse(text)
    print('2:format_tree')
    print(tree.toString(CaboCha.FORMAT_TREE))
    print('3.format_lattice') 
    print(tree.toString(CaboCha.FORMAT_LATTICE))   

if __name__  == '__main__':
    main()

"""
1:parseToString
  太郎は-----------D
      この-D       |
        本を---D   |
        次郎を-D   |
            見た-D |
            女性に-D
            渡した。
EOS

2:format_tree
  太郎は-----------D
      この-D       |
        本を---D   |
        次郎を-D   |
            見た-D |
            女性に-D
            渡した。
EOS

3.format_lattice
* 0 6D 0/1 -2.457381
太郎    名詞,固有名詞,人名,名,*,*,太郎,タロウ,タロー
は      助詞,係助詞,*,*,*,*,は,ハ,ワ
* 1 2D 0/0 1.532201
この    連体詞,*,*,*,*,*,この,コノ,コノ
* 2 4D 0/1 0.091699
本      名詞,一般,*,*,*,*,本,ホン,ホン
を      助詞,格助詞,一般,*,*,*,を,ヲ,ヲ
* 3 4D 1/2 2.132370
次      名詞,一般,*,*,*,*,次,ツギ,ツギ
郎      名詞,一般,*,*,*,*,郎,ロウ,ロー
を      助詞,格助詞,一般,*,*,*,を,ヲ,ヲ
* 4 5D 0/1 1.416783
見      動詞,自立,*,*,一段,連用形,見る,ミ,ミ
た      助動詞,*,*,*,特殊・タ,基本形,た,タ,タ
* 5 6D 0/1 -2.457381
女性    名詞,一般,*,*,*,*,女性,ジョセイ,ジョセイ
に      助詞,格助詞,一般,*,*,*,に,ニ,ニ
* 6 -1D 0/1 0.000000
渡し    動詞,自立,*,*,五段・サ行,連用形,渡す,ワタシ,ワタシ
た      助動詞,*,*,*,特殊・タ,基本形,た,タ,タ
。      記号,句点,*,*,*,*,。,。,。
EOS
"""