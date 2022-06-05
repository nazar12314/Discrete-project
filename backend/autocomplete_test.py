"""
    Comparing handmade autocomplete service, with ready realisation from MongoDB
"""

from Trie import Trie
import json
from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient


load_dotenv(find_dotenv())
password = os.environ.get("MONGODB_PWD")
connection = f"mongodb+srv://nazar:{password}@cluster0.y2vlb.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection)


def get_data(file):
    with open(file) as f:
        data = json.load(f)
    return data


def create_trie(data):
    trie = Trie()
    counter = 0
    for item in data:
        trie.insert(item["name"])
        if counter == 5000:
            break
    return trie


def mongo_autocomplete(query):
    database = client.DiscreteProject
    collection = database.SimpleData
    result = collection.aggregate([
        {
        "$search": {
            "index": "Autocomplete",
            "autocomplete": {
                "query": query,
                "path": "name",
                "tokenOrder": "sequential"
            }
        }
        }
    ])
    return list(result)


if __name__ == "__main__":
    data = get_data("cities.json")
    trie = create_trie(data)
    print(trie.search("Lv"))
    print(mongo_autocomplete("lv"))
