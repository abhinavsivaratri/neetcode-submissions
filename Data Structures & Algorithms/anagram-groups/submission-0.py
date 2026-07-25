class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)
        for i in strs:
            sortedS = ''.join(sorted(i))
            results[sortedS].append(i)
        return list(results.values())
