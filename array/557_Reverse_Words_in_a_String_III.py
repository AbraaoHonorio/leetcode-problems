class Solution:
    def reverseWords(self, s: str) -> str:
        left = 0
        right = 1
        result = ""
        while(right<len(s)):
            if(right!=len(s) and s[right] != " "):
                right+=1
            else:
                right+=1
                current_str = s[left:right]
                current_str_inverse = current_str[::-1]
                result = result + current_str_inverse
                left=right
                
        current_str_inverse = s[left:right][::-1]
        if result[1::]:
            result =  result[1::] + " " +  current_str_inverse 
            return result
        return current_str_inverse
