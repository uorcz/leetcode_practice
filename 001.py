#!/usr/bin/env python
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dictMap = {}
        for index, value in enumerate(num):
            if target - value in dictMap:
                return dictMap[target - value] + 1, index + 1
            dictMap[value] = index

# Old Solution

class Solution:
	def twoSum(self, num, target):
		for i in range(len(num)):
			for j in range(len(num)-1):
				if num[j+1] == target - num[i]:
					return [i, j+1]
