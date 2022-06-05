import unittest
from Trie import Trie, Node


class TestCases:
    class TestNode(unittest.TestCase):
        def test_empty_node_properties(self):
            n = Node()
            self.assertEqual(n.data, None, 'data property expected to be None')
            self.assertFalse(n.terminal, 'terminal property expected to be False')
            self.assertTrue(not n.children, 'children property length expected to be 0')

        def test_nonempty_node_properties(self):
            n = Node(terminal=True, data='k')
            child = Node(data='m')
            n.children['m'] = child
            self.assertEqual(n.data, 'k')
            self.assertTrue(n.terminal, 'terminal property expected to be True')
            self.assertTrue(len(n.children) == 1, 'children property length expected to be 1')
            self.assertIn(child, n.children.values())

    class TestTrie(unittest.TestCase):

        def test_init(self):
            trie = Trie()
            root = trie._root
            self.assertTrue(isinstance(root, Node))

            def assert_root_is_empty():
                self.assertEqual(root.data, None, 'data property expected to be None')
                self.assertFalse(root.terminal, 'terminal property expected to be False')
                self.assertTrue(not root.children, 'children property length expected to be 0')

            assert_root_is_empty()

        def test_insert(self):
            trie = Trie()
            word = 'hello'
            trie.insert(word)
            temp = trie._root
            for char in word:
                self.assertIn(char, temp.children)
                temp = temp.children[char]

        def test_exists(self):
            trie = Trie()
            word = 'hello'
            trie.insert(word)
            self.assertTrue(trie.exists(word))
            self.assertFalse(trie.exists(word[::-1]))

        def test_search(self):
            trie = Trie()
            word_list = ["hello", "help", "hello world!"]
            for word in word_list:
                trie.insert(word)
            self.assertSetEqual(set(trie.search('h')), set(word_list))

        def test_height(self):
            trie = Trie()
            self.assertEqual(trie.height(), 0)
            trie.insert("hello world!")
            self.assertEqual(trie.height(), 12)


def suiteNode():
    case = TestCases()
    suite = unittest.TestSuite()
    suite.addTests([case.TestNode('test_empty_node_properties'),
                    case.TestNode('test_nonempty_node_properties')])
    return suite


def suiteTrie():
    case = TestCases()
    suite = unittest.TestSuite()
    suite.addTests([case.TestTrie('test_init'),
                    case.TestTrie('test_insert'),
                    case.TestTrie('test_exists'),
                    case.TestTrie('test_search'),
                    case.TestTrie('test_height')])
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suiteNode())
    runner.run(suiteTrie())