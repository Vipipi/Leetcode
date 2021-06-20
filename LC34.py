class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchfirst():
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = l + (r - l)// 2
                if nums[mid] == target:
                    if (mid-1 >= 0 and nums[mid-1] != target) or mid == 0:
                        return mid
                    r = mid - 1
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
            return -1
        def searchlast():
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = l + (r - l)// 2
                if nums[mid] == target:
                    if (mid+1 < len(nums) and nums[mid+1] != target) or mid == len(nums)-1:
                        return mid
                    l = mid + 1
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
            return -1
        
        return [searchfirst(),searchlast()]
        
        
        
        
        
        
