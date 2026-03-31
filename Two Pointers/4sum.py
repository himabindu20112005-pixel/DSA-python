#leetcode 18 4Sum
#Difficulty: Medium
from ast import List



class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        if n < 4:  # Early exit for insufficient length
            return res

        for i in range(n - 3):
            # Skip duplicate for i
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Pruning 1: If smallest possible sum with nums[i] is already greater than target, break
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            
            # Pruning 2: If largest possible sum with nums[i] is less than target, continue
            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target:
                continue

            for j in range(i + 1, n - 2):
                # Skip duplicate for j
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                # Pruning 3: If smallest possible sum with nums[i] and nums[j] is greater than target, break
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break

                # Pruning 4: If largest possible sum with nums[i] and nums[j] is less than target, continue
                if nums[i] + nums[j] + nums[n-2] + nums[n-1] < target:
                    continue


                left = j + 1
                right = n - 1

                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if current_sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        # Skip duplicates for left
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        # Skip duplicates for right
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1

                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
        return res
# Time Complexity: O(n^3) in the worst case due to three nested loops and two-pointer traversal
# Space Complexity: O(1) if we don't count the output list, otherwise O(k
