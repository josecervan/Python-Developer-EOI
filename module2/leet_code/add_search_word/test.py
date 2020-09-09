from trie import WordDictionary
import unittest


class Test(unittest.TestCase):

    def test_add_word(self):
        wd = WordDictionary()

        self.assertIsNone(wd.add_word('bad'))
        self.assertIsNone(wd.add_word('dad'))
        self.assertIsNone(wd.add_word('mad'))
        
    def test_search(self):
        wd = WordDictionary()

        wd.add_word('bad')
        wd.add_word('dad')
        wd.add_word('mad')

        self.assertFalse(wd.search('pad'))
        self.assertFalse(wd.search('p..'))
        self.assertFalse(wd.search('.'))
        self.assertFalse(wd.search(''))
        self.assertFalse(wd.search('....'))

        self.assertTrue(wd.search('bad'))
        self.assertTrue(wd.search('.ad'))
        self.assertTrue(wd.search('b..'))
        self.assertTrue(wd.search('...'))


if __name__ == '__main__':
    unittest.main()
