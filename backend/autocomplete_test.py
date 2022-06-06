"""
    Comparing handmade autocomplete service, with ready realisation from MongoDB
"""

from Trie import Trie
import json
from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient
from datetime import datetime
from suffix_tree import SuffixTree


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
        if counter == 10000:
            break
    return trie


def create_text_dataset():
    index = 0
    result = {}
    with open("text.txt") as file:
        for line in file.readlines():
            if line == "\n":
                index += 1
                continue
            result[index] = result.get(index, "") + line.rstrip("\n")
    return result


def full_text_search(data, query):
    result = []
    for item in data:
        suffix_tree = SuffixTree(data[item])
        if suffix_tree.search_pattern(query):
            result.append(item)
    return result


def mongo_full_text_search(query):
    database = client.TextSearch
    collection = database.SimpleData
    result = collection.aggregate([
        {
            "$search": {
                "index": "text_search",
                "text": {
                    "query": query,
                    "path": "item"
                }
            }
        }
    ])
    return list(result)


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
    cities_data = get_data("cities.json")
    dataset = create_text_dataset()
    trie = create_trie(cities_data)
    start = datetime.now()
    trie.search("Ol")
    print(f"Autocomplete using Trie: {datetime.now() - start}")
    start = datetime.now()
    mongo_autocomplete("Ol") 
    print(f"Autocomplete using MongoDB: {datetime.now() - start}")
    start = datetime.now()
    mongo_full_text_search("am")
    print(f"Full text search using MongoDB: {datetime.now() - start}")
    start = datetime.now()
    full_text_search(dataset, "am")
    print(f"Full text search using Suffix tree: {datetime.now() - start}")

