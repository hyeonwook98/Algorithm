def solution(nums):
    max = len(nums)/2
    count=1
    number=0
    nums.sort()
    for i in range(len(nums)-1):
        number=nums[i]
        if(number!=nums[i+1]):
            count+=1
    if(count>=max):
        return max
    else:
        return count
