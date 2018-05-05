import os
import string
import time
from urllib import request as ur
from urllib import parse as up
from bs4 import BeautifulSoup as bs
import lxml

#from wikiscraper import *
#from gutenscraper import *
from replacements import *

included_chs = string.ascii_letters + string.digits + string.punctuation + ' '

def unicode_lookup(symbol):
    url = 'http://graphemica.com/' + up.quote(symbol)
    req = ur.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    document = ur.urlopen(req).read()
    soup = bs(document, 'lxml')
    return soup.title.text

def pretty_dict(dictionary, wrap_length):
    keys = list(dictionary.keys())
    lines = []
    
    for i in range(len(keys)//wrap_length+1):
        try:
            line = ["%s: %s, " % (repr(key),repr(dictionary[key])) for key in keys[wrap_length*i:wrap_length*i+wrap_length]]
            lines.append(''.join(line))
        except IndexError:
            line = ["%s: %s, " % (repr(key),repr(dictionary[key])) for key in keys[wrap_length*i:]]
            lines.append(''.join(line))
    return '{' + '\n'.join(lines) + '}'

def write_replacements():
    sorted_ascii_replacements = dict(sorted(ascii_replacements.items(), key=lambda t: t[0]))
    with open('replacements.py','w',encoding='utf-8') as fh:
        fh.write('ascii_replacements = ' + pretty_dict(sorted_ascii_replacements,7))

def sources(path):
    full_path = 'sources/%s/' % path
    return [full_path + file for file in os.listdir(full_path)]

def collect_group(group):
    corpus = ''
    articles = sources(group)
    
    for file in articles:
        if os.path.isfile(file):
            print('Transferring %s...' % file)
            with open(file,'r',encoding='utf-8') as fh:
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

    return {'name':group,'corpus':corpus,'sources':len(articles),'size':len(corpus)}

    print('Collected %d sources.' % len(articles))
    print('Corpus has %d characters.' % len(corpus))

def collect_all():
    start_time = time.time()
    groups = ['wikipedia','gutenberg']
    corpora = [collect_group(group) for group in groups]
    combined_corpus = ' '.join([corpus['corpus'] for corpus in corpora])
    print()
    for corpus in corpora:
        print('Group %s:' % corpus['name'])
        percent = round(corpus['size']*100/len(combined_corpus))
        print('\tSize: %d (%d percent)' % (corpus['size'],percent))
        print('\tNumber of sources: %s' % corpus['sources'])

    print()
    print('Total corpus size: %d' % len(combined_corpus))
    with open('corpus.txt','w',encoding='utf-8') as fh:
        fh.write(combined_corpus)
    elapsed = int(time.time() - start_time)
    print('Took %d seconds.' % elapsed)

collect_all()
