from flask import Flask, jsonify, request
from Trie import Trie
from suffix_tree import SuffixTree
import csv

app = Flask(__name__)

trie = Trie()

def fill_tree_with_data(file):
    with open(file) as file:
        csvreader = csv.reader(file)
        for idx, row in enumerate(csvreader):
            if idx != 0:
                trie.insert(row[1].lower())


def create_suffix_tree(file):
    with open(file) as f:
        result = " ".join([line.replace("\n", "") for line in f.readlines()])
    suffix_tree = SuffixTree(result)
    return suffix_tree

fill_tree_with_data("data.csv")
suffix_tree = create_suffix_tree("text.txt")

@app.route('/api')
def api():
    query = request.args.get('search')
    if query:
        return jsonify([{"id": idx, "value": value} for idx, value in enumerate(trie.search(query))])
    return jsonify([{}])


@app.route("/text")
def home():
    query = request.args.get('search')
    if query:
        return jsonify({"data": suffix_tree.search_pattern(query)})
    return jsonify({})
