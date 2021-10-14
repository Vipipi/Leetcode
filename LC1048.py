"""backtracking"""
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_dict = collections.defaultdict(list)
        
        for word in words:
            for i in range(len(word)):
                key = word[:i] + "*" + word[i+1:]
                word_dict[key].append(word)
                
        res = 0
        
        def bt(next_word, count):
            nonlocal res
            res = max(count, res)
            
            for i in range(len(next_word)+1):
                dummy = list(next_word)
                dummy.insert(i, "*")
                key = "".join(dummy)
                if key in word_dict:
                    for w in word_dict[key]:
                        bt(w, count + 1)
        
        for word in words:
            bt(word, 1)
            
        return res
    
"""Dynamic Programming"""
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if len(words) == 1:
            return 1
        dp = collections.defaultdict(int)
        res = 0
        words.sort(key = lambda x: len(x))
        for word in words:
            if len(word) == 1:
                dp[word] = 1
            else:
                local_max = 0
                for i in range(len(word)):
                    key = word[:i] + word[i+1:]
                    local_max = max(local_max, dp[key])
                dp[word] = local_max + 1
                res = max(res, dp[word])
                        
        return res
