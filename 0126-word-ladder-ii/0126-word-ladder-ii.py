class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        # BFS setup
        queue = deque([beginWord])
        prev_words = defaultdict(list)  # for reconstructing paths
        distance = {beginWord: 0}
        found = False
        word_len = len(beginWord)
        
        while queue and not found:
            next_level_visited = set()
            for _ in range(len(queue)):
                current = queue.popleft()
                for i in range(word_len):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == current[i]:
                            continue
                        next_word = current[:i] + c + current[i+1:]
                        if next_word in wordSet:
                            if next_word not in distance:
                                distance[next_word] = distance[current] + 1
                                queue.append(next_word)
                                next_level_visited.add(next_word)
                            if distance[next_word] == distance[current] + 1:
                                prev_words[next_word].append(current)
                            if next_word == endWord:
                                found = True
            wordSet -= next_level_visited
        
        # Recursive backtracking to build paths
        def backtrack(word, path):
            if word == beginWord:
                result.append([beginWord] + path[::-1])
                return
            for prev in prev_words[word]:
                backtrack(prev, path + [word])
        
        result = []
        if found:
            backtrack(endWord, [])
        return result