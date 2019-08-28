#! /usr/bin/env python
# encoding:utf-8

# 論文IDだけを抽出
# 参考サイト：
# https://qiita.com/EN-0/items/59af824aa24db23ec96a

import urllib.request
from xml.etree.ElementTree import *

keyword = 'cancer'
baseURL = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term='

def get_id(url):
    result  = urllib.request.urlopen(url)
    return result

def main():
    url = baseURL + keyword
    result  = get_id(url)
    element = fromstring(result.read())
    for line in element.findall('.//Id'):
        print(line.text)

if __name__ == '__main__':
    main()
