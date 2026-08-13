class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)

        if (endWord not in word_set or not endWord or not beginWord or len(endWord) != len(beginWord)):
            return []

        level = deque([(beginWord)])

        prev_words = defaultdict(list)
        found = False
        while level and not found:
            level_visited = set()
            next_level = deque()
            sz = len(level)
            for _ in range(sz):
                curr_word = level.popleft()

                for i, ch in enumerate(curr_word):
                    for letter in string.ascii_lowercase:
                        if ch == letter:
                            continue

                        next_word = curr_word[:i] + letter + curr_word[i+1:]

                        if next_word in word_set:
                            if next_word == endWord:
                                found = True
                            prev_words[next_word].append(curr_word)
                            if next_word not in level_visited:
                                level_visited.add(next_word)
                                next_level.append((next_word))

            level = next_level
            word_set -= level_visited

        
        res = []

        print(prev_words)

        def backtrack(word, path):
            print(path)
            if word == beginWord:
                sequence = path + [beginWord]
                res.append(sequence[::-1])
                return 

            for prev in prev_words[word]:
                backtrack(prev, path + [word])

        if found:
            backtrack(endWord, [])

        return res