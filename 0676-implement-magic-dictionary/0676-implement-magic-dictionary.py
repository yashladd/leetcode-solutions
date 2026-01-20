class MagicDictionary:

    def __init__(self):
        self.words = set()

    def buildDict(self, dictionary: List[str]) -> None:
        self.words = set(dictionary)
        

    def search(self, searchWord: str) -> bool:
        # print(self.words)
        for i in range(len(searchWord)):
            for ch_ord in range(ord('a'), ord('a') + 26):
                if chr(ch_ord) != searchWord[i]:
                    changedWord = searchWord[:i] + chr(ch_ord) + searchWord[i+1:]
                    # print(changedWord, str(ch_ord))
                    if changedWord in self.words:
                        return True
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)