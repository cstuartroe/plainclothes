from urllib import request as ur
from bs4 import BeautifulSoup as bs
import lxml
import re
import os
import time           

stories = [{'name':'Dracula',
            'path':'cache/epub/345/pg345.txt',
            'start':'CHAPTER I JON',
            'end':'THE END'},
           {'name':'Grimm_Fairytales',
            'path':'files/2591/2591-0.txt',
            'start':'THE GOLDEN BIRD A certain',
            'end':'reading ever since.'},
           {'name':'Moby_Dick',
            'path':'files/2701/2701-0.txt',
            'start':'CHAPTER 1. Loomings. Call',
            'end':'another orphan.'},
           {'name':'A_Tale_Of_Two_Cities',
            'path':'files/98/98-0.txt',
            'start':'I. The Period It was',
            'end':'have ever known.”'},
           {'name':'Pride_And_Prejudice',
            'path':'files/1342/1342-0.txt',
            'start':'Chapter 1 It is a',
            'end':'uniting them.'},
           {'name':'Sherlock_Holmes',
            'path':'cache/epub/1661/pg1661.txt',
            'start':'ADVENTURE I.',
            'end':'considerable success.'},
           {'name':'War_And_Peace',
            'path':'files/2600/2600-0.txt',
            'start':'CHAPTER I “Well, Prince',
            'end':'not conscious.'}]

def gutenscrape(story):
    url = 'http://www.gutenberg.org/' + story['path']
    text = ur.urlopen(url).read().decode('utf-8')
    text = text.replace('\r',' ')
    text = text.replace('\n',' ')
    text = text.replace('\xa0',' ')
    text = re.sub(' +',' ',text)
    start_index = text.index(story['start'])
    end_index = text.index(story['end']) + len(story['end'])
    text = text[start_index:end_index]

    with open('sources/gutenberg/' + story['name'] + '.txt','w',encoding='utf-8') as fh:
        fh.write(text)

    return text

def gutenscrape_all(stories):
    start_time = time.time()
    folder = 'sources/gutenberg/'
    if not os.path.isdir(folder):
        os.makedirs(folder)
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        if os.path.isfile(file_path):
            os.unlink(file_path)
    
    for story in stories:
        print('Scraping %s...' % story['name'])
        gutenscrape(story)

    print('Scraped %d articles.' % len(stories))
    elapsed = int(time.time() - start_time)
    print('Took %d seconds.' % elapsed)

gutenscrape_all(stories)
