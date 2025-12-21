class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        wordSet = set(wordDict)
        sentences = []
        
        def get_sentences(i, sentence):
            if i == n:
                sentences.append(" ".join(sentence))
                return 
            
            
            for j in range(i+1, n+1):
                currWord = s[i:j]
                if currWord in wordSet:
                    get_sentences(j, sentence + [currWord])
                    
                    
        get_sentences(0, [])
        
        return sentences
                
                
        
        