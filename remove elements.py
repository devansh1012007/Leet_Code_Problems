# Restart 
#rethink the problem
'''
class Solution(object):
    def removeElement(self, nums, val):
        if not nums:  # Handle empty list case
            return 0
        #nums.sort()
        placer =len(nums)-1
        for i in range(0, len(nums)-1):
            if nums[i] == val:
                nums[i], nums[placer] = nums[placer], nums[i]
                placer = placer - 1
            
            if i == placer:
                return i -1
                break
            #i =+1
        
        #return i # error #IDK WHY
'''
# make the abobe in reverse 
class Solution(object):
    def removeElement(self, nums, val):
        if not nums:  # Handle empty list case
            return 0
        #nums.sort()
        placer = 1
        while nums[-placer] == val:
            placer = placer + 1 
        i = placer + 1
        while i <= len(nums):
            if nums[-i] == val:
                nums[-i], nums[-placer] = nums[-placer], nums[-i]
                placer = placer + 1
                i =+ 1
            
            
        return i - 1
        #i =+1
        
        #return i # error

# think of  a sitiation where u don't change anything if val comes



































'''class Solution(object):
    def removeElement(self, nums, val):
        if not nums:  # Handle empty list case
            return 0

        #improve it from here 
        k = len(nums) - 1
        j = 0  # Pointer for the position of unique elements
        for i in range(0, k): # 
            print (nums)
            if nums[i] != val: # 
                j += 1  # Move to the next position for unique element
                nums[j] = nums[i]  # Assign the unique element
            continue
        return j + 1
    
'''
'''
BULSHIT CODES

#rethink the problem
class Solution(object):
    def removeElement(self, nums, val):
        if not nums:  # Handle empty list case
            return 0

        #improve it from here 
        j = 0  # Pointer for the position of unique elements
        for i in range(1, len(nums)): # 
            if nums[i] != val: # 
                j += 1  # Move to the next position for unique element
                nums[j] = nums[i]  # Assign the unique element

        return j + 1

        

class Solution:
    def removeDuplicates(self, arr, nums):
        if not nums:  # Handle empty list case
            return 0
        #improve it from here
        j = 0  # Pointer for the position of unique elements
        for i in range(1, len(arr)):
            if nums[j] == : # nums  
                j += 1  # Move to the next position for unique element
                nums[j] = nums[i]  # Assign the unique element
        return j + 1  # Return the length of the list with unique element
'''
'''

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
''' 
'''
# problem with this code is that it can't determine 1st val
class Solution(object):
    def removeElement(self, nums, val):
        if not nums:  # Handle empty list case
            return 0
        nums.sort()
        if nums[0] == val and len(nums) == 1:
            return 0
        #improve it from here 
        #k = len(nums) - 1
        j = 0  # Pointer for the position of unique elements
        for i in range(1, len(nums)): # 
            print (nums, i , j)
            if nums[i] != val: # 
                j += 1  # Move to the next position for unique element
                nums[j] = nums[i]  # Assign the unique element
            #continue
        return j + 1
'''

'''
# pop method
class Solution(object):
    def removeElement(self, nums, val):
        if not nums:  # Handle empty list case
            return 0
        nums.sort()
        #improve it from here 
        k = len(nums) - 1
        #j = 0  # Pointer for the position of unique elements
        for i in range(0, k): # 
            if nums[i] == val: # 
                #j += 1  # Move to the next position for unique element
                nums.pop(i)
                #nums[j] = nums[i]  # Assign the unique element     
            continue

        return len(nums)

'''
'''
class Solution(object):
    def removeElement(self, nums, val):
        if not nums:  # Handle empty list case
            return 0
        
        nums.sort()
        #improve it from here 
        #k = len(nums) - 1
        j = 0  # Pointer for the position of unique elements
        for i in range(1, len(nums)): # 
            print (nums, i , j)
            if nums[i] != val: # 
                j += 1  # Move to the next position for unique element
                nums[j] = nums[i]  # Assign the unique element
            #continue
        return j+1
'''
