class WordDictionary:

    def __init__(self):
        self.lst = list()

    def add_word(self, word: str) -> None:
        if word not in self.lst:
            self.lst.append(word)

    def search(self, word: str) -> bool:
        if '.' not in word:
            return word in self.lst

        lenw = len(word)
        lenlst = len(self.lst)

        idx_lst = 0
        while idx_lst < lenlst:
            idx_word = 0
            if lenw == len(self.lst[idx_lst]):
                while idx_word < lenw and (word[idx_word] == '.' or word[idx_word] == self.lst[idx_lst][idx_word]):
                    idx_word += 1

                if idx_word == lenw:
                    return True

            idx_lst += 1

        if idx_lst == lenlst:
            return False
