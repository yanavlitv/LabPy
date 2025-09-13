def twosum(nums, target):
    a = []
    for i in nums:
        if isinstance(i, int) == True:
            a.append(target - i)
        else:
            return None
    for i in range(len(a)):
        k = nums[i+1:]
        if a[i] in k:
            ind = k.index(a[i]) + i +1
            return [i, ind]
    return None

n = [-1, -4, 'р']
t = -5
print(twosum(n, t))