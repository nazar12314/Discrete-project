class Node:
    def __init__(self, position=None, length=None):
        """
        Node class
        :param position: index of letter from original line
        :param length: length of subword
        e.g. if position = 4, length = 2 and word is "Ukraine" then edge is "in" (word[4:4+2])
        """
        self.position: int = position
        self.length: int = length
        self.children = {}

    def __repr__(self):
        return f"({self.position}, {self.length})"


class SuffixTree:
    def __init__(self, word):
        self._root = Node()  # root node is always empty
        self.word = None
        self.remake(word)

    def node_str(self, node):
        """Returns which letters node represents"""
        if node is None: return ""
        return self.word[node.position:node.position+node.length]

    def add_subword(self, subword):
        """
        Adds subword(suffix) from main word to tree.
        """
        def recursive_adder(start_node, subword_):
            for node in start_node.children.values():
                children_str = self.node_str(node)
                if subword_[0] == children_str[0]:
                    for i in range(min(len(subword_), len(children_str))):
                        if subword_[i] != children_str[i]:
                            # ріжимо поточний нод
                            node.children[node.position+i] = (Node(node.position+i, node.length-i))
                            node.length = i
                            # додаємо порізаний subword
                            node.children[len(self.word) - len(subword_) + i] = (Node(len(self.word) - len(subword_) + i, len(subword_) - i))
                            return
                    # якщо subword довший за строку у ноді, то продовжуємо пошук у дітей цього ноду з меншим subword'ом
                    recursive_adder(node, subword_[len(children_str):])
                    return
            # або створюємо нову дитину у кореня
            start_node.children[len(self.word) - len(subword_)] = (Node(len(self.word) - len(subword_), len(subword_)))
        recursive_adder(self._root, subword)

    def remake(self, word):
        """
        Builds tree from given word.
        Can be used to rebuild tree from new word.
        """
        word_with_zero = word + "0"
        self._root = Node()
        self.word = word_with_zero
        for i in range(len(word_with_zero) - 1, -1, -1):
            self.add_subword(word_with_zero[i:len(word_with_zero)])

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
                    result += self.node_str(node.children[child]) + "\n"
            return result

        return recursive_helper(self._root, 0)

    def search_pattern(self, pattern):
        """
        Returns the positions of each match within the text
        """
        def recursive_search(stat_node, pattern_, walked_length=0):
            matches = []
            for child_ind, child_node in stat_node.children.items():
                child_str = self.node_str(child_node)
                if child_str.startswith(pattern_) or pattern_.startswith(child_str):
                    if not child_node.children:
                        # print(child_ind-walked_length)
                        matches += [child_ind-walked_length]
                    else:
                        matches += recursive_search(child_node, pattern_[len(child_str):], len(child_str)+walked_length)
            return matches
        return recursive_search(self._root, pattern)


# example of use
if __name__ == "__main__":
    tree = SuffixTree("banana")
    print(tree.search_pattern("ana")) # [6, 1]
    # rebuild tree
    tree.remake("bbb")
    print(tree.search_pattern("bb")) # [1, 0]
