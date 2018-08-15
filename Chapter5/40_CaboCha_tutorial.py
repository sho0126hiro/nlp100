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