class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        while(left <= right):
            mid = left + (right - left)//2
            if(nums[mid] == target):
                return mid
            #if left part is sorted
            if(nums[mid] >= nums[left]):
                #if target is on left sorted part
                if(target >= nums[left] & target < nums[mid]):
                    right = mid-1
                else:
                    left = mid+1
            else:
                #if target is on right sorted part
                if(target > nums[mid] & target <= nums[right]):
                    left = mid +1
                else:
                    right = mid -1
        return -1