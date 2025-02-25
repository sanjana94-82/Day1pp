#find sec_largest
def sec_largest(nums):
    nums.sort()
    for num in range(len(nums)-1,-1,-1):
        if nums[num]<nums[-1]:
            return nums[num]
l1=[1,2,5,6,9,3,9]
print(sec_largest(l1))