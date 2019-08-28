#! /usr/bin/env python
# encoding:utf-8

# DATE      : 2019-08-28

# IDから論文summaryを取得
# 参考サイト
# https://qiita.com/EN-0/items/59af824aa24db23ec96a

import urllib.request
from xml.etree.ElementTree import *

keyword = 'cancer'
idfile  = 'idlist_' + keyword + '.txt'
baseURL = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id='

def get_xml(url):
    result  = urllib.request.urlopen(url)
    return result

def main():
    idlist  = []
    f       = open(idfile, 'r')
    for i in f.readlines():
        idlist.append(i.strip())
    f.close()
    url     = baseURL + idlist[0]
    result  = get_xml(url)
    print(result.read())


if __name__ == '__main__':
    main()
