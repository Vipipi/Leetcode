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
