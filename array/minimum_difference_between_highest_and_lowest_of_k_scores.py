class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        minimum_difference = nums[len(nums)-1]
        k = k - 1
        for start in range(len(nums)-k):
            minimum_difference = min(minimum_difference, nums[start+k] - nums[start])
        return minimum_difference
