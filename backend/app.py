from flask import Flask, jsonify, request
from Trie import Trie
import csv

app = Flask(__name__)

trie = Trie()

def fill_tree_with_data(file):
    with open(file) as file:
        csvreader = csv.reader(file)
        for idx, row in enumerate(csvreader):
            if idx != 0:
                trie.insert(row[1].lower())

fill_tree_with_data("data.csv")


@app.route('/api')
def api():
    query = request.args.get('search')
    if query:
        return jsonify([{"id": idx, "value": value} for idx, value in enumerate(trie.search(query))])
    return jsonify([{}])
