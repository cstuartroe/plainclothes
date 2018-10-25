from urllib import request as ur
from urllib import parse as up
from bs4 import BeautifulSoup as bs
import re
import os
import time
import string

included_chs = string.ascii_letters + string.digits + string.punctuation + ' '

replacements_filepath = os.path.join(os.path.dirname(__file__),"replacements")

def read_replacements():
        replacements_dict = {}
        with open(replacements_filepath,"r",encoding="utf-8") as fh:
            lines = fh.readlines()
        for line in lines:
            char = line[0]
            repl = line[2:-1]
            replacements_dict[char] = repl
        return replacements_dict

def write_replacements(replacements_dict):
    replacements_list = list(replacements_dict.items())
    replacements_list = sorted(replacements_list, key=lambda x: x[0])
    lines = [(char + " " + repl) for char, repl in replacements_list]
    with open(replacements_filepath,"w",encoding="utf-8") as fh:
        fh.write("\n".join(lines))

def unicode_lookup(symbol):
    url = 'http://graphemica.com/' + up.quote(symbol)
    req = ur.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    document = ur.urlopen(req).read()
    soup = bs(document, 'lxml')
    return soup.title.text

def ascii_sub(string):
    output = ""
    ascii_replacements = read_replacements()
    for ch in string:
        try:
            newseq = ascii_replacements[ch]
            try:
                assert(all(newch in included_chs for newch in newseq))
            except AssertionError:
                raise KeyError
        except KeyError:
            print('Unknown Char: ' + unicode_lookup(ch))
            newseq = input('Replacement: ')
            ascii_replacements[ch] = newseq
        output += newseq

    write_replacements(ascii_replacements)
    return output

class Reader:
    def __init__(self):
        self.sources_dir = os.path.join(os.path.dirname(__file__),'../sources/',self.name)
        if not os.path.isdir(self.sources_dir):
            os.makedirs(self.sources_dir)
        for file in os.listdir(self.sources_dir):
            filepath = os.path.join(self.sources_dir, file)
            if os.path.isfile(filepath):
                os.unlink(filepath)
        print("Initialized reader " + self.name)

    def read(self,source):
        url = os.path.join(self.url_root, source["path"])

        try:
            document = ur.urlopen(url).read()
        except TimeoutError:
            print("Request timed out. Retrying...")
            return self.read(source)
            
        text = self.get_text(document,source)
        text = ascii_sub(text)
        text = re.sub('\s+',' ',text)

        filepath = os.path.join(self.sources_dir,source["name"]+".txt")
        with open(filepath, "w", encoding='utf-8') as fh:
            fh.write(text)

        print("Success")

    def read_all(self):
        start_time = time.time()
        
        for source in self.sources:
            print('Reading %s...' % source['name'])
            self.read(source)

        print('Read %d articles.' % len(self.sources))
        elapsed = int(time.time() - start_time)
        print('Took %d seconds.' % elapsed)
