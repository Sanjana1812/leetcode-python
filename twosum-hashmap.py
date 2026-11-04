Two sum using hash-map method

nums = [2,7]
target = 9
seen ={}
for i in range(len(nums)):
  current_number = nums[i]
  complement = target - current_number
  if complement in seen:
    print([seen[complement],i])
seen[current_number]=i
