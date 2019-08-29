#! /usr/bin/env python
# encoding:utf-8

# DATE      : 2019-08-28

# 論文IDだけを抽出
# 参考サイト：
# https://qiita.com/EN-0/items/59af824aa24db23ec96a

import urllib.request
from xml.etree.ElementTree import *

# single keyword,   keyword = 'cancer'
# multiple keyword, keyword = 'cancer+colon'
# Data range, two parameters : mindate, maxdate
keyword = 'cancer+colon'
baseURL = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term='


def get_id(url):
    result  = urllib.request.urlopen(url)
    return result

def main():
    url = baseURL + keyword
    result      = get_id(url)
    element     = fromstring(result.read())
    filename    = 'idlist_' + keyword + '.txt'
    f   = open(filename, 'w')
    for line in element.findall('.//Id'):
        f.write(line.text + '\n')
    f.close()

if __name__ == '__main__':
    main()
