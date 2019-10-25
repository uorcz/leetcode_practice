#!/usr/bin/env python
class Solution:
    # @return a string
    def grayCode(self, n: int) -> List[int]:
        return [i ^ i >> 1  for i in range(1 << n)]