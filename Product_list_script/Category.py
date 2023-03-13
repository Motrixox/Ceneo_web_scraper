import requests
from bs4 import BeautifulSoup


class Category:
    def __init__(self, category, link):
        self.category = category
        self.link = link
        self.id_list = []
        self.name_list = []

    def download(self):
        download_html = requests.get(self.link)

        soup = BeautifulSoup(download_html.text, features="html.parser")
        with open('downloaded.html', 'w', encoding="utf-8") as file:
            file.write(soup.prettify())

        for x in range(30):
            try:
                self.name_list.append(soup.select('div.js_man-track-event')[x].get("data-productname").__str__())
            except():
                self.name_list.append("Cannot get the name")
                continue

        for x in range(30):
            try:
                self.id_list.append(soup.select('div.js_man-track-event')[x].get("data-productid").__str__())
            except():
                self.id_list.append("Cannot get the id")
                continue

    def get_object(self, i):
        result_object = {
            "id" : self.id_list[i],
            "category" : self.category,
            "name" : self.name_list[i]
        }
        return result_object

