from flask import Flask, jsonify, request
from Trie import Trie

app = Flask(__name__)

trie = Trie()
trie.insert("parrot")
trie.insert("pray")
trie.insert("parad")
trie.insert("hello")
trie.insert("help")
trie.insert("hello world!")
trie.insert("hello my friend!")
trie.insert('hi how are you?')
trie.insert('hijab')
trie.insert('hola')
trie.insert("how do do?")

@app.route('/api')
def api():
    query = request.args.get('search')
    if query:
        return jsonify([{"id": idx, "value": value} for idx, value in enumerate(trie.search(query))])
    return jsonify([{}])


if __name__ == '__main__':
    app.run(debug=True, port=8080)
