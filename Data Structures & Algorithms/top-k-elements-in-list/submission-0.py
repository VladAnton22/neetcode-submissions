class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        for n, c in counts.items():
            frequency[c].append(n)

        result = []

        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                result.append(n)
                if len(result) == k:
                    return result

