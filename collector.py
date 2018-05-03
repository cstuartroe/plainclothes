import os
import string
import time
from urllib import request as ur
from urllib import parse as up
from bs4 import BeautifulSoup as bs
import lxml

#from wikiscraper import *
from replacements import *

included_chs = string.ascii_letters + string.digits + string.punctuation + ' '

def unicode_lookup(symbol):
    url = 'http://graphemica.com/' + up.quote(symbol)
    req = ur.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    document = ur.urlopen(req).read()
    soup = bs(document, 'lxml')
    return soup.title.text

def write_replacements():
    sorted_ascii_replacements = str(dict(sorted(ascii_replacements.items(), key=lambda t: t[0])))
    split = sorted_ascii_replacements.split(', ')
    lines = []
    for i in range(len(split)//7+1):
        try:
            lines.append(', '.join(split[7*i:7*i+7]))
        except IndexError:
            lines.append(', '.join(split[7*i:]))
    with open('replacements.py','w',encoding='utf-8') as fh:
        fh.write('ascii_replacements = ' + ',\n'.join(lines))

def collect():
    start_time = time.time()
    corpus = ''
    folder = 'sources'
    articles = os.listdir(folder)
    
    for the_file in articles:
        file_path = os.path.join(folder, the_file)
        if os.path.isfile(file_path):
            print('Transferring %s...' % the_file)
            with open(file_path,'r',encoding='utf-8') as fh:
                text = fh.read() + ' '
            for ch in text:
                try:
                    newseq = ascii_replacements[ch]
                    try:
                        assert(all(newch in included_chs for newch in newseq))
                    except AssertionError:
                        raise KeyError
                    corpus += newseq
                except KeyError:
                    try:
                        print('Unknown Char: ' + unicode_lookup(ch))
                        replacement = input('Replacement: ')
                        if replacement == 'exit':
                            write_replacements()
                            print('%d entries in ascii_replacements.' % len(ascii_replacements.keys()))
                            raise KeyError
                        corpus += replacement
                        ascii_replacements[ch] = replacement   
                    except UnicodeEncodeError:
                        pass
                    
            write_replacements()

    print('Collected %d sources.' % len(articles))
    print('Corpus has %d characters.' % len(corpus))
    with open('corpus.txt','w',encoding='utf-8') as fh:
        fh.write(corpus)
    elapsed = int(time.time() - start_time)
    print('Took %d seconds.' % elapsed)

collect()
