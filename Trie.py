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

    def insert(self, word: str) -> None:
        """Inserts a word into the Trie

        Args:
            word (str): a word to insert
        """
        temporary: Node = self._root

        for char in word:
            if char not in temporary.children:
                temporary.children[char] = Node()
            temporary = temporary.children[char]
        temporary.terminal = True

    def search(self, word: str) -> bool:
        """Checks word for a presence in a tree

        Args:
            word (str): a word to search for

        Returns:
            Boolean: whether a word is present in the tree
        """
        temporary = self._root

        for char in word:
            if char not in temporary.children:
                return False
            temporary = temporary.children[char]
        return True

    def height(self, node=None):
        """
        Returns height of the tree
        """
        if node is None:
            node = self._root
        if not node.children:
            return 0
        else:
            return 1 + max(self.height(node.children[child]) for child in node.children)
        

    def __str__(self) -> str:
        """
        String representation of a tree
        """
        def recurse(node: Node, level: int) -> str:
            """
            Recursive helper function for str
            """
            result = ""
            if node is not None:
                for child in node.children:
                    result += recurse(node.children[child], level + 1)
                    result += "| " * level
                    result += str(child) + "\n"
            return result

        return recurse(self._root, 0)
