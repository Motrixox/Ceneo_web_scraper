import Product
import datetime
from pymongo import MongoClient


def get_collection(name):
    CONNECTION_STRING = "SECRET MONGODB CONNECTION STRING"
    client = MongoClient(CONNECTION_STRING)
    return client['Data'][name]


item_list = []
object_list = []

product_list_collection = get_collection('Product_list')
price_list_collection = get_collection('Price_list')

product_list = product_list_collection.find()

for product in product_list:
    item_list.append(Product.Product(product['id']))

i = 1
print('download progress:')
for item in item_list:
    item.download()
    print(datetime.datetime.now().__str__()[:-7] + '  |  ' + i.__str__() + ' out of 300 ' + item.get_object()[
        'price'].__str__())
    object_list.append(item.get_object())
    i += 1

print(datetime.datetime.now().__str__()[:-7] + '  |  ' + 'sending to database...')

price_list_collection.insert_many(object_list)

print(datetime.datetime.now().__str__()[:-7] + '  |  ' + 'DONE!!!')
