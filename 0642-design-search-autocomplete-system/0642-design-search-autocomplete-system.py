class Node:
    def __init__(self):
        self.children = {}
        self.sentences = defaultdict(int)

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = Node()
        self.curr_sentence = []
        self.curr_node = self.root
        for s, cnt in zip(sentences, times):
            self._add_sentence(s, cnt)

    def input(self, c: str) -> List[str]:
        if c == "#":
            self._add_sentence("".join(self.curr_sentence), 1)
            self.curr_sentence = []
            self.curr_node = self.root
            return []

        if c not in self.curr_node.children:
            self.curr_node.children[c] = Node()
            self.curr_sentence.append(c)
            self.curr_node = self.curr_node.children[c]
            return []
        
        self.curr_node = self.curr_node.children[c]
        self.curr_sentence.append(c)
        # self.curr_node = self.curr_node.children[ch]
        res = heapq.nsmallest(3, [(x[1], x[0]) for x in self.curr_node.sentences.items()])
        return [x[1] for x in res]

    def _add_sentence(self, sentence, cnt):
        curr = self.root
        for ch in sentence:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
            curr.sentences[sentence] -= cnt


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)