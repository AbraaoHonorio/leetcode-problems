#https://leetcode.com/problems/minimum-size-subarray-sum/description/
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        current_window_sum = 0
        window_start = 0
        min_window_size = sys.maxsize
        for window_end, value in enumerate(nums):
            current_window_sum += value
            while(current_window_sum >= target):
                min_window_size = min(min_window_size,window_end - window_start +1)
                current_window_sum -= nums[window_start]
                window_start+=1

        if min_window_size == sys.maxsize:
            return 0
        return min_window_size
