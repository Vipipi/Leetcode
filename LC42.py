""""first attempt"""
class Solution:
    def trap(self, height: List[int]) -> int:
        start_h = 0
        end_h = 0
        start_idx = 0
        end_idx = 0
        accum = 0
        for curr_idx in range(0,len(height)):
            if (height[curr_idx] >= start_h):
                end_idx = curr_idx
                end_h = height[curr_idx]
                for j in range(start_idx, end_idx+1):
                    if min(start_h,end_h) >= height[j]:
                        accum += min(start_h,end_h) - (height[j])
                        print  (accum)
                start_h = height[curr_idx]
                start_idx = curr_idx
        
        height.reverse()
        start_h = 0
        end_h = 0
        start_idx = 0
        end_idx = 0
        for curr_idx in range(0,len(height)):
            if (height[curr_idx] > start_h):
                end_idx = curr_idx
                end_h = height[curr_idx]
                for j in range(start_idx, end_idx+1):
                    if min(start_h,end_h) > height[j]:
                        accum += min(start_h,end_h) - (height[j])
                        print  (accum)
                start_h = height[curr_idx]
                start_idx = curr_idx
        
        
        return accum