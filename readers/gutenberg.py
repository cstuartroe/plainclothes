from reader import Reader
import re

stories = [{'name':'Dracula',
            'path':'cache/epub/345/pg345.txt',
            'start':'CHAPTER I JON',
            'end':'THE END'},
           {'name':'Grimm Fairytales',
            'path':'files/2591/2591-0.txt',
            'start':'THE GOLDEN BIRD A certain',
            'end':'reading ever since.'},
           {'name':'Moby Dick',
            'path':'files/2701/2701-0.txt',
            'start':'CHAPTER 1. Loomings. Call',
            'end':'another orphan.'},
           {'name':'A Tale Of Two Cities',
            'path':'files/98/98-0.txt',
            'start':'I. The Period It was',
            'end':'have ever known.”'},
           {'name':'Pride And Prejudice',
            'path':'files/1342/1342-0.txt',
            'start':'Chapter 1 It is a',
            'end':'uniting them.'},
           {'name':'Sherlock Holmes',
            'path':'cache/epub/1661/pg1661.txt',
            'start':'ADVENTURE I.',
            'end':'considerable success.'},
           {'name':'War And Peace',
            'path':'files/2600/2600-0.txt',
            'start':'CHAPTER I “Well, Prince',
            'end':'not conscious.'}]

class GutenbergReader(Reader):
    def __init__(self,_sources=stories):
        self.name = "gutenberg"
        self.url_root = 'http://www.gutenberg.org/'
        self.sources = _sources
        super(GutenbergReader,self).__init__()

    def get_text(self,document,story):
        text = document.decode("utf-8")
        text = re.sub('\s+',' ',text)
        start_index = text.index(story['start'])
        end_index = text.index(story['end']) + len(story['end'])
        return text[start_index:end_index]
