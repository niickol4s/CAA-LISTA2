def merge(nums1, m, nums2, n):
  i = 0
  j = 0
  k = 0

  while i < m and j < n:
    if nums1[i] <= nums2[j]:
      nums1[k] = nums1[i]
      i += 1
    else:
      nums1[k] = nums2[j]
      j += 1
    k += 1

  if i == m:
    for j in range(j, n):
      nums1[k] = nums2[j]
      k += 1
  else:
    for i in range(i, m):
      nums1[k] = nums1[i]
      k += 1

  return nums1

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

nums1 = merge(nums1, m, nums2, n)

print(nums1)
