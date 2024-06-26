class Solution:
    def removeElement(self, nums, val):
        # Initialize a variable to keep track of the index of elements to remove
        remove_index = 0
        
        for index in range(len(nums)):
            # If the current element is not equal to val, keep it and move it to the front of the list
            if nums[index] != val:
                nums[remove_index] = nums[index]
                remove_index += 1

        nums = nums[:remove_index]       
        

        return len(nums)

# Test the function
obj = Solution()
nums = [3, 2, 2, 3]
val = 3
result = obj.removeElement(nums, val)
print("The length of the modified list:", result)
print("The modified list:", nums) 
