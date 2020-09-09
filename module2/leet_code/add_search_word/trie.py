N_CHARACTERS = 26


class WordDictionary:

    def __init__(self):
        self.root = [None] * N_CHARACTERS
        self.is_end_of_word = False

    def add_word(self, word: str) -> None:
        current = self
        for c in word:
            if current.root[ord(c) - ord('a')] is None:
                current.root[ord(c) - ord('a')] = WordDictionary()
            current = current.root[ord(c) - ord('a')]

        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        current = self
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for ch in current.root:
                    if (ch is not None) and (ch.search(word[i + 1:])):
                        return True
                return False

            if current.root[ord(c) - ord('a')] is None:
                return False
            current = current.root[ord(c) - ord('a')]

        return (current is not None) and current.is_end_of_word
