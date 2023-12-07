def majoritario(nums):
  count = 1
  majoritario = nums[0]

  for i in range(1, len(nums)):
    if nums[i] == majoritario:
      count += 1
    elif nums[i] != majoritario:
      count -= 1
      if count == 0:
        majoritario = nums[i]
        count = 1

  return majoritario

nums = [1, 1, 1, 2, 2, 2, 3]

majoritario = majoritario(nums)

print(majoritario)
