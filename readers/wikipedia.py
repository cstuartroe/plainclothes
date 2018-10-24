from reader import Reader
from urllib import parse as up
from bs4 import BeautifulSoup as bs
import re

articles = []
article_names = ['China','India','United States','Indonesia','Pakistan','Brazil','Nigeria','Bangladesh',
            'Russia','Japan','Mexico','Philippines','Egypt','Ethiopia','Vietnam','Germany','Iran',
            'Democratic Republic of the Congo','Turkey','Thailand','United Kingdom','France',
            'Italy','Canada','South Korea','Australia','Spain','Netherlands','Saudi Arabia','Switzerland',
            'European Union',
            'Tokyo','Yokohama','Jakarta','Delhi','Manila','Seoul','Karachi','Shanghai','Mumbai',
            'New York City','São Paulo','Beijing','Mexico City','Guangzhou','Foshan',
            'Osaka','Dhaka','Moscow','Cairo','Bangkok','Los Angeles','Buenos Aires','Kolkata',
            'Tehran','Istanbul','Lagos','Tianjin','Shenzhen','Rio de Janeiro','Kinshasa',
            'Lima','Chengdu','Paris','Lahore','Bangalore','London','Ho Chi Minh City','Chennai',
            'Nagoya','Bogotá','Hyderabad','Chicago','Johannesburg','Taipei',
            'Facebook','Youtube','Google','Wikipedia','Apple Inc.','Microsoft','Amazon.com',
            'Donald Trump','Barack Obama','Adolf Hitler','Abraham Lincoln','Theresa May',
            'Narendra Modi','Chuck Schumer','Julian Assange','James Comey','Kim Jong Un',
            'Xi Jinping','Rodrigo Duterte','Vladimir Putin','Pope Francis','Recep Tayyip Erdoğan',
            'Juan Manuel Santos','Vajiralongkorn','Qasem Soleimani',
            'Lady Gaga','Eminem','The Beatles','Steve Jobs','Elizabeth II','Cristiano Ronaldo',
            'Stephen Hawking','Lil Wayne','Rihanna','Selena Gomez','Taylor Swift','Lionel Messi',
            'Albert Einstein','Johnny Depp','Melinda Gates','Chance the Rapper','Constance Wu',
            'Janet Yellen','Lebron James','Jeff Bezos','Indra Nooyi',
            'Earth','Sun','Moon','Star',
            'Mathematics','Science','History','Writing',
            'World War I','World War II',]

for article_name in article_names:
    articles.append({"name":article_name,"path":up.quote(article_name.replace(" ","_"))})

class WikipediaReader(Reader):
    def __init__(self,_sources=articles):
        self.name = "wikipedia"
        self.url_root = 'https://en.wikipedia.org/wiki/'
        self.sources = _sources
        super(WikipediaReader,self).__init__()

    def get_text(self,document,source):
        soup = bs(document, 'lxml')
        body = soup.find('div',{'class':'mw-parser-output'})
        #body.find('div',{'id':'toc'}).decompose()
        paras = [para.text for para in body.find_all('p')]
        text = '\n'.join(paras)
        text = re.sub(r'\[[0-9]*\]','',text)
        return text
