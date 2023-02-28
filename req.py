import requests
import json
from bs4 import BeautifulSoup as bs
from random import randint
from data import config


class Auto_request:
    def __init__(self):
        self.link = []
        self.auto_list = []
        self.url = config.url

    def requests_get(self):
        response = requests.get(self.url)
        return bs(response.text, 'lxml')

    def link_cleaning(self):
        container_link = self.requests_get().findAll(class_='lazyload')
        for i in container_link:
            get_link = i.get("data-src")
            if get_link.startswith('https:'):
                self.link.append(get_link)
        return self.link

    def auto_cleaning(self):
        container_auto = self.requests_get().findAll('div', class_='text')
        for i_auto in container_auto:
            self.auto_list.append({'AUTO': i_auto.find(class_="title").text,
                                   'RUN': i_auto.find(class_="run").text,
                                   'ENGINE': i_auto.find(class_="engine").text,
                                   'YEAR_OF_ISSUE': i_auto.find(class_="props").find().text,
                                   'FUEL': ''.join(i_auto.find(class_="props").text.split(','))[17:36],
                                   'LINK': [self.link[i:i + 4] for i in range(0, len(self.link_cleaning()), 4)]
                                   [len(self.auto_list)],
                                   'PRICE': round(randint(2000000, 10000000), -4)
                                   }
                                  )
        return self.auto_list

    def run(self):
        with open('../Новая папка/TELEGRAM_BOT_AUTO/data/parser.json', 'w') as file:
            json.dump(self.auto_cleaning(), file, indent=4, ensure_ascii=False)


auto = Auto_request()
auto.run()
