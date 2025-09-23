'''class Solution(object):
    def removeDuplicates(self, arr):
        arr = self.arr
        n = len(arr)
        if n <= 1:
            return n

        # Start from the second element
        idx = 1  #will point to the next unique element position
        
        for i in range(1, n):
            if arr[i] != arr[i - 1]:# Check if the current element is not a duplicate
                arr[idx] = arr[i]# Move unique element forward this won't matter till the pointer
                #enconters atleast 1 duplicate as the val of idx will be same as i
                idx += 1# Increment the index for the next unique element
        
        j = 0
        while j < n:
            arr.append(0)
            j = j + 1
        return n , arr
        # idk what this code is asking , idk how they want the return format'''

## not mine
class Solution:
    def removeDuplicates(self, nums):
        if not nums:  # Handle empty list case
            return 0

        j = 0  # Pointer for the position of unique elements
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1  # Move to the next position for unique element
                nums[j] = nums[i]  # Assign the unique element

        return j + 1  # Return the length of the list with unique elements