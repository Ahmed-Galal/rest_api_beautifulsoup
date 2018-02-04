#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import re


class Util():

    def has_img(self,tag):
        if (tag.has_attr('class') and not tag.has_attr('style')):
            if ("item_imagePic" in tag.get('class')):
                return True
        return False

    def fixString(self,txt):
        txt = re.sub("'", '`', txt)
        # txt = re.sub("\n", '', txt)
        return txt

    def getUrl(self,url):
        print("===getUrl==")
        print(url)
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def item_json_object(self,item):
        data = {
            'availabilityStarts': self.fixString(item.find('p', itemprop='availabilityStarts').text) if item.find('p', itemprop='availabilityStarts') else '',
            'description': self.fixString(item.find('p', itemprop='description').text) if item.find('p', itemprop='description') else '',
            'city': self.fixString(item.find('span', itemprop='address').text) if item.find('span', itemprop='address') else '',
            'Honoraires': item.find('span',text=re.compile('Honoraires')).find_next_sibling("span").text if item.find('span',text=re.compile('Honoraires')) else '',
            'Reference': item.find('span',text=re.compile('rence')).find_next_sibling("span").text if item.find('span',text=re.compile('rence')) else '',
            'GES': item.find('span',text=re.compile('GES')).find_next_sibling("span").text if item.find('span',text=re.compile('GES')) else '',
            'Classe_energie': item.find('span',text=re.compile('nergie')).find_next_sibling("span").text if item.find('span',text=re.compile('nergie')) else ''
        }
        return data

    def json_object(self,item,item_url):
        i_url = item_url.replace('{ITEMID}',item.find('div', class_='saveAd').get('data-savead-id'))
        soup = self.getUrl(i_url)
        item_json = self.item_json_object(soup.find('section', class_="adview_main"))
        data = {
            "img": self.fixString(item.find('span', class_='lazyload').get('data-imgsrc') if item.find(self.has_img) else ''),
            "title": self.fixString(item.find('h2', class_='item_title').text) if item.find('h2', class_='item_title') else '',
            "price": self.fixString(item.find('h3', class_='item_price').text) if item.find('h3', class_='item_price') else '',
            "date": self.fixString(item.find('p', itemprop='availabilityStarts').get('content')) if item.find('p', itemprop='availabilityStarts') else '',
            "id": self.fixString(item.find('div', class_='saveAd').get('data-savead-id')) if item.find('div', class_='saveAd') else '',
            "url": i_url,
            'availabilityStarts': item_json['availabilityStarts'],
            'description': item_json['description'],
            'city': item_json['city'],
            'postal_code': item_json['city'].split(' ')[1] if item_json['city'] else '',
            'Honoraires': item_json['Honoraires'],
            'Reference': item_json['Reference'],
            'GES': item_json['GES'],
            'Classe_energie': item_json['Classe_energie'],
        }
        return data