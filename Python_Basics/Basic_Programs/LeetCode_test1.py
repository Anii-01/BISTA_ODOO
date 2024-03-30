nums = [1,3,5,6]
target = 7

def Fun1(nums , target):

    for index in range(0,len(nums)):
                if nums[index] == target:
                    return index
                
                elif (target > nums[len(nums)-1]):
                    return len(nums)
                
                else:
                    if(target > nums[index]) and (target < (nums[index+1])):
                        #List.insert(index+1,target)
                        return index+1
               
result = Fun1(nums,target)
print(result)