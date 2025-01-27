#https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        current_window_sum = 0
        window_start = 0
        max_sum = 0
        counter = {}
        for window_end, value in enumerate(nums):
            current_window_sum += value
            window_size = window_end - window_start + 1 
            if counter.get(value, None):
                counter[value] += 1
            else:
                counter[value] = 1
            
            while counter[value] > 1 or window_size > k:
                counter[nums[window_start]] = counter[nums[window_start]] - 1
                current_window_sum -= nums[window_start]
                window_start+=1
                window_size = window_end - window_start +1

            if window_size == k:
                max_sum = max(max_sum, current_window_sum)
    
    
        return max_sum
