import requests
import datetime
import time
import json
from bs4 import BeautifulSoup


class Product:
    def __init__(self, _id):
        self.id = _id
        self.link = "https://m.ceneo.pl/" + _id
        self.price = 0.0
        self.tries = 0

    def download(self):
        download_html = ''
        while download_html == '' and self.tries < 3:
            try:
                download_html = requests.get(self.link)
            except:
                self.tries += 1
                time.sleep(5 * self.tries)
                continue

        if download_html == '':
            self.price = -1.0
            return

        soup = BeautifulSoup(download_html.text, features="html.parser")

        try:
            json_object = json.loads(soup.select('script[type="application/ld+json"]')[0].text)
            self.price = json_object['offers']['lowPrice']
        except:
            if self.tries < 2:
                self.tries += 1
                time.sleep(5 * self.tries)
                self.download()
            pass

    def get_object(self):
        result_object = {
            "id" : self.id,
            "date" : datetime.datetime.now().date().__str__(),
            "time" : datetime.datetime.now().time().__str__()[:-7],
            "price" : self.price
        }
        return result_object

