class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Understanding:
        # put all anagrams(who has the exact same number of same letters) in to a same array
        # Ex: aa bb ab ba -< [aa], [bb], [ab, ba]

        res = defaultdict(list)
        for str in strs:
            count = [0] * 26

            for c in str: 
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(str)
        print(res)

        return res.values()

            
