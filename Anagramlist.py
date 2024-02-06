strs = ['a']
if len(strs)==0:
    print([[""]])
else:
    res = []
    for i in strs:
        for j in range(len(res)):
            if len(res[j])>0 and sorted(i) == sorted(res[j][0]):
                res[j].append(i)
                break
        else:
            res.append([i]) 
    print(sorted(res,key=len))  

'''
class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())
'''
