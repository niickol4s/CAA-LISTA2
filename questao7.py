def quadrados(nums):
  n = len(nums)
  res = [0 for _ in range(n)]

  for i in range(n):
    res[i] = nums[i] * nums[i]

  return sorted(res)

nums = [-4, -1, 0, 3, 10]

quadrados = quadrados(nums)

print(quadrados)
