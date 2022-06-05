# Discrete-project

## To launch a project

#### Clone it from the repo
```shell
git clone https://github.com/nazar12314/Discrete-project.git .
```
#### Install node modules
```shell
npm run deploy
```

#### Run the server
```shell
npm run dev
```

At this point you will be able to observe a project opened in your browser. It includes two main functionalities: autocomplete service and text search through a document.

### Example of text search

https://user-images.githubusercontent.com/59284695/172040783-3b3a59dd-5724-499b-b492-9cb7d7457717.mov

### Example of autocomplete

https://user-images.githubusercontent.com/59284695/172040839-a8b44f15-c17e-475d-bc3e-e7e006bb7068.mov

The program consists of two parts:
 - Backend (All logic of the project, including trees representation and server. All the code implemented with python, server runs using Flask)
 - Frontend (Vizualisation of the project. Implemented using react js.)

## Implemented data structures

In this project we implemented two tree-type data structures - Prefix tree (general form of Trie) and Suffix tree (compresed from of Trie)

### Prefix tree

Preffix tree of Trie is a tree constructed to work with strings. In general it is a tree where every node is a single letter.

#### To create a Prefix tree
```python
tree = Trie()
```
#### After we can insert some words into it
```python
tree.insert("and")
tree.insert("ant")
tree.insert("cat")
```
#### At this point our tree looks like this
                      "t"
        "a" -> "n" -> 
                      "d"              
  | 

        "c" -> "a" -> "t"
                      
#### Search in a Trie
To search, we write a query 
```python
tree.search("a") ## "a" is a query
```
Result:
```shell
["and", "ant"]
```

### Suffix tree
<Roma>
