def pipe_fix():
    nums = [1,3,4,6,7,8]
    for i in enumerate(nums):
        nums += 1
        print(nums[i])
pipe_fix()