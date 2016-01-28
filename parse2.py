#!/usr/bin/env python                                                                                                                                             
# -*- coding:utf-8 -*-                                                                                                                                            

import MeCab
import SearchWord   # hand-made external file

### Constants                                                                                                                                                     
MECAB_MODE = 'mecabrc'
PARSE_TEXT_ENCODING = 'utf-8'

### Functions                                                                                                                                                     
def main():
    tweets = SearchWord.getTweet(query="レシピ",limit=10)
    text = tweets[0]
    words_dict = parse(text)
    print "Nouns:", ",".join(words_dict)
    return


def parse(unicode_string):
    tagger = MeCab.Tagger(MECAB_MODE)
    # str 型じゃないと動作がおかしくなるので str 型に変換
    text = unicode_string.encode(PARSE_TEXT_ENCODING)
    node = tagger.parseToNode(text)

    nouns = []
    while node:
        pos = node.feature.split(",")[0]
        # unicode 型に戻す
        word = node.surface.decode("utf-8")
        if pos == "名詞":
            nouns.append(word)
        node = node.next
    return nouns

### Execute                                                                                                                                                       
if __name__ == "__main__":
    main()
