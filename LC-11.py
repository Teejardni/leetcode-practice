class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        i = 0
        j = len(height) - 1
        while i != j:
            ans = max(ans, (min(height[i],height[j])*(abs(i-j))))
            if height[i] > height[j]:
                j = j-1
            else:
                i += 1
        return ans

