class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] = count[num] + 1
            else:
                count[num] = 1
        
        sorted_array = []
        
        for num,freq in count.items():
            sorted_array.append([num,freq])
        sorted_array.sort(key=lambda row: row[1], reverse=True)

        results = []
        for row in sorted_array[:k]:
            results.append(row[0])
        return results
                