from typing import Dictionary


class Node:
    def __init__(self, data=None, terminal: bool = False) -> None:
        """
        arg: children -> dictionary of children of the given Node
        arg: terminal -> boolean value to check whether a node is an end of the word
        """
        self.terminal: bool = terminal
        self.data: str = data
        self.children: Dictionary = {}


class Trie:
    def __init__(self) -> None:
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
                temporary.children[char] = Node(data=char)
            temporary = temporary.children[char]
        temporary.terminal = True

    def exists(self, word) -> bool:
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

    def search(self, query: str) -> list:
        """Searches for words that match given query

        Args:
            query (str): given query

        Returns:
            list: list of words that match given query
        """
        if not self.exists(query):
            return []

        result = []
        temporary: Node = self._root

        for char in query:
            temporary = temporary.children[char]        

        def depth_first_search(node: Node, prefix: str) -> None:
            """Helper function for iterating through the deep of a tree.

            Args:
                node (Node): a starting point
                prefix (str): a string that has already been formed
            """
            if node.terminal:
                result.append(prefix + node.data)

            for child in node.children.values():
                depth_first_search(child, prefix + node.data)

        depth_first_search(temporary, query[:-1])

        return result

    def height(self, node=None) -> int:
        """
        Returns height of the tree
        """
        if node is None:
            node = self._root
        if not node.children:
            return 0
        else:
            return 1 + max(self.height(node.children[child]) for child in node.children)

    def delete(self, word: str) -> bool:
        pass

    def __str__(self) -> str:
        """
        String representation of a tree
        """
        def recursive_helper(node: Node, level: int) -> str:
            """
            Recursive helper function for str
            """
            result = ""
            if node is not None:
                for child in node.children:
                    result += recursive_helper(node.children[child], level + 1)
                    result += "| " * level
                    result += str(child) + "\n"
            return result

        return recursive_helper(self._root,  0)
