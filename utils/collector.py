import os
import time
from readers.wikipedia import WikipediaReader
from readers.gutenberg import GutenbergReader

all_readers = {"wikipedia":WikipediaReader,"gutenberg":GutenbergReader}

def source_filepaths(reader_name):
    full_path = os.path.join(os.path.dirname(__file__),"../sources",reader_name)
    full_path = os.path.normpath(full_path)
    return [os.path.join(full_path,file) for file in os.listdir(full_path)]

def collect_sources(reader_name):
    print("Collecting group %s..." % reader_name)
    corpus = ''
    filepaths = source_filepaths(reader_name)
    for filepath in filepaths:
        print('Transferring %s...' % filepath)
        with open(filepath,'r') as fh:
            corpus += "\n" + fh.read()
    return {'name':reader_name,'corpus':corpus,'sources':len(filepaths),'size':len(corpus)}

def download(reader_names=[]):
    if reader_names == []:
        reader_names = all_readers.keys()

    for reader_name in reader_names:
        reader = all_readers[reader_name]()
        reader.read_all()

def collect_all():
    start_time = time.time()
    corpora = []
    for reader_name in all_readers.keys():
        corpora.append(collect_sources(reader_name))
        
    combined_corpus = ''.join([corpus['corpus'] for corpus in corpora])
    print()
    for corpus in corpora:
        print('Group %s:' % corpus['name'])
        percent = round(corpus['size']*100/len(combined_corpus))
        print('\tSize: %d (%d percent)' % (corpus['size'],percent))
        print('\tNumber of sources: %s' % corpus['sources'])

    print()
    print('Total corpus size: %d' % len(combined_corpus))

    corpus_filepath = os.path.join(os.path.dirname(__file__),"../sources/corpus.txt")
    with open(corpus_filepath,'w',encoding='utf-8') as fh:
        fh.write(combined_corpus)

    elapsed = int(time.time() - start_time)
    print('Took %d seconds.' % elapsed)
