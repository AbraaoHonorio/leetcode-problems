# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        result = 0
        while(left<right):
            result = numbers[right] + numbers[left]
            if(result == target):
                return [left + 1, right + 1]
            if result > target:
                right-=1
                left = 0
            else:
                left+=1