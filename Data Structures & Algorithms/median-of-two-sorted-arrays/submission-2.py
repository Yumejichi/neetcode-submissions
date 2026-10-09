class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # find the mid val of mid1 and mid2
        # we use l, r and do binary search to find the idx where all left is left side and right for right side
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        Aleft, Aright, Bleft, Bright = 0, 0, 0, 0
        l, r = 0, len(nums1)
        half = (len(nums1) + len(nums2)) // 2
        while l <= r:
            a_right_start = (l+r) // 2 # left side has a_right_start elements
            b_right_start = half - a_right_start # a_right_start+b_right_start = half (left elemnts sum is half)

            Aleft = nums1[a_right_start-1] if a_right_start-1>=0 else float("-inf")
            Aright = nums1[a_right_start] if a_right_start < len(nums1) else float("inf")

            Bleft = nums2[b_right_start-1] if b_right_start-1 >= 0 else float("-inf")
            Bright = nums2[b_right_start] if b_right_start < len(nums2) else float("inf")

            # compare
            if Aleft <= Bright and Bleft <= Aright:
                # this is the one we want:
                if (len(nums1) + len(nums2))%2 == 0:
                    return (max(Aleft,Bleft) + min(Bright, Aright))/2
                else:
                    return min(Aright, Bright)

            elif Aright > Bleft:
                r = a_right_start-1 
            else:
                l = a_right_start + 1
        