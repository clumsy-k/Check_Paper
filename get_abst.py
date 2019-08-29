#! /usr/bin/env python
# encoding:utf-8

# DATE      : 2019-08-28

# 論文の要旨を取得
# 参考サイト
# https://qiita.com/EN-0/items/59af824aa24db23ec96a

import urllib.request
from xml.etree.ElementTree import *

# keyword = 'cancer'
keyword = 'cancer+colon'
idfile  = 'idlist_' + keyword + '.txt'
baseURL = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id='

def get_xml(url):
    result  = urllib.request.urlopen(url)
    return result

def main():
    idlist  = []
    f       = open(idfile, 'r')
    for i in f.readlines():
        idlist.append(i.strip())
    f.close()
    url     = baseURL + idlist[0] + '&retmode=xml'
    result  = get_xml(url)
    element = fromstring(result.read())
    for line in element.findall('.//AbstractText'):
        print(line.text)


if __name__ == '__main__':
    main()
