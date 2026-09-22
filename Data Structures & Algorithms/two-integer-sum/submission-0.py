class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in index:
                return [index[diff], i]
            else:
                index[n] = i
