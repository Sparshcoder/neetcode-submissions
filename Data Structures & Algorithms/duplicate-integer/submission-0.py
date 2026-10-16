class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = set(nums)
        if len(nums) != len(x):
            return True
        else:
            return False
        