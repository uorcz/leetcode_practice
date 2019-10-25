#!/usr/bin/env python
class Solution:
    # @return a string
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    	nums1[m:m+n] = nums2      # 将nums2合并到nums1中
        nums1.sort() 