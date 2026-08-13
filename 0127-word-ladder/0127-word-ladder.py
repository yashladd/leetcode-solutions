class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set=set(wordList)

        if endWord not in word_set:
            return 0

    
        frontier = deque([(beginWord, 1)])
        seen = {beginWord}
        while frontier:
            curr_word, steps = frontier.popleft()

            
            for i, ch in enumerate(curr_word):
                for letter in string.ascii_lowercase:
                    next_word = curr_word[:i] + letter + curr_word[i+1:]
                    if next_word == endWord:
                        return steps + 1
                    if next_word in word_set and next_word not in seen:
                        seen.add(next_word)
                        frontier.append((next_word, steps + 1))

        return 0


