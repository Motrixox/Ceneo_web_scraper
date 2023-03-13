import Category
from pymongo import MongoClient


def get_collection(name):
    CONNECTION_STRING = "SECRET MONGODB CONNECTION STRING"
    client = MongoClient(CONNECTION_STRING)
    return client['Data'][name]


product_list_collection = get_collection('Product_list')

item_list = []
object_list = []

text_file = open("items.txt", "r")

while True:
    try:
        data = text_file.readline().split(',')
        item_list.append(Category.Category(data[0], data[1]))
    except:
        break

print('downloading...')

for item in item_list:
    item.download()
    for x in range(30):
        object_list.append(item.get_object(x))

print('sending to database...')

product_list_collection.insert_many(object_list)

print("DONE!!!")
