from collections import defaultdict
def countPalindromicSubsequence(self, s: str) -> int:
        count = defaultdict(list)

        for index,ch in enumerate(s):
            if ch not in count:
                count[ch].extend([index,0])
            else:
                count[ch][1] = index

        palindrom_count = 0

        for ch in count:
            i,j = count[ch]
            if i<j:
                palindrom_count+=len(set((s[i+1:j])))


        return (palindrom_count)
