#https://leetcode.com/problems/optimal-partition-of-string/description/
class Solution:
    def partitionString(self, s: str) -> int:
        current_substring = set()
        num_substring = 1

        for value in s:
            if not value in current_substring:
                current_substring.add(value)
                continue

            num_substring+=1
            current_substring = set()
            current_substring.add(value)
         
        
        return num_substring
