class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        cache = {}
        
        def break_word(s):
            if s not in cache:
                result = []
                for w in wordDict:
                    if s[:len(w)] == w:
                        if len(s) == len(w):
                            result.append(w)
                        else:
                            for word in break_word(s[len(w):]):
                                result.append(w + " " + word)
                cache[s] = result
            return cache[s]
        
        return break_word(s) 
