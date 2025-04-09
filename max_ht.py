class Solution:
    def maxArea(self, height: list[int]) -> int:
        r = len(height) -1
        l = 0
        max_area = 0
        while(l<r):
            max_area = max(max_area, min(height[l], height[r])*(r-l))
            if(height[l] < height[r]):
                l += 1
            else:
                r -= 1
        return max_area
print(Solution().maxArea([1,3,10,8]))