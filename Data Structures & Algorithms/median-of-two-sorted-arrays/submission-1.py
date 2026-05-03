class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        

        def find_k_th_element(i, j, k):
            # base case
            
            if i >= len(nums1):
                # nums1 exhausted, return nums2's kth elem
                return nums2[j + k -1]
            
            if j >= len(nums2):
                return nums1[i + k - 1]
            if k == 1:
                return min(nums1[i], nums2[j])

            # revursive part
            half_k = k // 2

            nums1_mid_value =  nums1[i + half_k - 1]
            nums2_mid_value = nums2[j + half_k - 1]

            # check which is smaller and eliminate half of them
            if nums1_mid_value < nums2_mid_value:
                # eliminate the left half of the nums1
                return find_k_th_element(i+half_k, j, k - half_k)
            else:
                return find_k_th_element(i, j+half_k, k - half_k)
            
        
        m, n = len(nums1), len(nums2)

        left_median = find_k_th_element(0, 0, (m+n+1)//2)
        right_median = find_k_th_element(0, 0, (m+n+2)//2)

        return float(left_median + right_median) / 2
