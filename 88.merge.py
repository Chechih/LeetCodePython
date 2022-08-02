from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        rlt = nums1[:m] + nums2[:n]
        rlt.sort()
        nums1[:] = [r for r in rlt]