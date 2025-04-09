class Solution:
    def search(self,nums,target,serch_right):
        left = 0
        right = len(nums) - 1
        idx = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                idx = mid
                if not serch_right:
                    right = mid - 1
                else:
                    left = mid + 1
        return idx

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = self.search(nums,target,False)
        right = self.search(nums,target,True)
        return [left, right]