#!/usr/bin/env python                                                                                                                                             
# -*- coding:utf-8 -*-                                                                                                                                            

import MeCab
import SearchWord   # hand-made external file

### Constants                                                                                                                                                     
MECAB_MODE = 'mecabrc'
PARSE_TEXT_ENCODING = 'utf-8'

### DATA
words = {}

### Functions                                                                                                                                                     
def main():
    # getting list
    tweets = SearchWord.getTweet(query="レシピ",limit=3000)

    for tweet in tweets:
        if "http" in tweet:
            tweet = tweet.split("http",1)[0] # deleting urls
        if "RT " in text:
            tweet = tweet.split(":",1)[1] # deleting RTs
        nouns = parse(tweet)
        counter(nouns)

    sortdict(words)
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

def counter(wordlist):
    for word in wordlist:
        words[word] = words.get(word, 0) + 1

def sortdict(dct):
    tmp = [(v,k) for k,v in dct.items()]
    tmp.sort()
    tmp.reverse()

    for count, word in tmp[:50]:
        print count, word

### Execute                                                                                                                                                       
if __name__ == "__main__":
    main()
