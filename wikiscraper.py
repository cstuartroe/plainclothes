from urllib import request as ur
from bs4 import BeautifulSoup as bs
import lxml
import re
import os
import time

articles = ['China','India','United_States','Indonesia','Pakistan','Brazil','Nigeria','Bangladesh',
            'Russia','Japan','Mexico','Philippines','Egypt','Ethiopia','Vietnam','Germany','Iran',
            'Democratic_Republic_of_the_Congo','Turkey','Thailand','United_Kingdom','France',
            'Italy','Canada','South_Korea','Australia','Spain','Netherlands','Saudi_Arabia','Switzerland',
            'European_Union',
            'Tokyo','Yokohama','Jakarta','Delhi','Manila','Seoul','Karachi','Shanghai','Mumbai',
            'New_York_City','S%C3%A3o_Paulo','Beijing','Mexico_City','Guangzhou','Foshan',
            'Osaka','Dhaka','Moscow','Cairo','Bangkok','Los_Angeles','Buenos_Aires','Kolkata',
            'Tehran','Istanbul','Lagos','Tianjin','Shenzhen','Rio_de_Janeiro','Kinshasa',
            'Lima','Chengdu','Paris','Lahore','Bangalore','London','Ho_Chi_Minh_City','Chennai',
            'Nagoya','Bogot%C3%A1','Hyderabad','Chicago','Johannesburg','Taipei',
            'Facebook','Youtube','Google','Wikipedia','Apple_Inc.','Microsoft','Amazon.com',
            'Donald_Trump','Barack_Obama','Adolf_Hitler','Abraham_Lincoln','Theresa_May',
            'Narendra_Modi','Chuck_Schumer','Julian_Assange','James_Comey','Kim_Jong_Un',
            'Xi_Jinping','Rodrigo_Duterte','Vladimir_Putin','Pope_Francis','Recep_Tayyip_Erdo%C4%9Fan',
            'Juan_Manuel_Santos','Vajiralongkorn','Qasem_Soleimani',
            'Lady_Gaga','Eminem','The_Beatles','Steve_Jobs','Elizabeth_II','Cristiano_Ronaldo',
            'Stephen_Hawking','Lil_Wayne','Rihanna','Selena_Gomez','Taylor_Swift','Lionel_Messi',
            'Albert_Einstein','Johnny_Depp','Melinda_Gates','Chance_the_Rapper','Constance_Wu',
            'Janet_Yellen','Lebron_James','Jeff_Bezos','Indra_Nooyi',
            'Earth','Sun','Moon','Star',
            'Mathematics','Science','History','Writing',
            'World_War_I','World_War_II',]

def wikiscrape(article_name):
    url = 'https://en.wikipedia.org/wiki/' + article_name
    document = ur.urlopen(url).read()
    soup = bs(document, 'lxml')
    body = soup.find('div',{'class':'mw-parser-output'})
    #body.find('div',{'id':'toc'}).decompose()
    paras = [para.text for para in body.find_all('p')]
    text = '\n'.join(paras)
    text = re.sub(r'\[.*?\]','',text)
    text = text.replace('\n',' ')
    text = text.replace('\xa0',' ')
    text = re.sub(' +',' ',text)

    with open('sources/wikipedia/' + article_name + '.txt','w',encoding='utf-8') as fh:
        fh.write(text)

    return text

def wikiscrape_all(articles):
    start_time = time.time()
    folder = 'sources/wikipedia'
    if not os.path.isdir(folder):
        os.makedirs(folder)
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        if os.path.isfile(file_path):
            os.unlink(file_path)
    
    for article in articles:
        print('Scraping %s...' % article)
        wikiscrape(article)

    print('Scraped %d articles.' % len(articles))
    elapsed = int(time.time() - start_time)
    print('Took %d seconds.' % elapsed)

wikiscrape_all(articles)
