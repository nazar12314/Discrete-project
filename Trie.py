class Node:
    def __init__(self, terminal: bool = False) -> None:
        """
        arg: children -> dictionary of children of the given Node
        arg: terminal -> boolean value to check whether a node is an end of the word
        """
        self.terminal = terminal
        self.children = {}


class Trie:
    def __init__(self):
        """
        Creates a root for a Trie
        """
        self._root = Node()

    def insert(self, text: str) -> None:
        temporary: Node = self._root

        for char in text:
            if char not in temporary.children:
                temporary.children[char] = Node()
            temporary = temporary.children[char]
        temporary.terminal = True

    def contains(self, text: str):
        temporary = self._root

        for char in text:
            if char not in temporary.children:
                return False
            temporary = temporary.children[char]
        return True
