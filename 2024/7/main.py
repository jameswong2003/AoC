p1 = 0
p2 = 0
D = open('data.txt').read().strip()

def is_valid(target, nums, p2):
    if len(nums) == 1:
        return nums[0]==target
    if is_valid(target, [nums[0] + nums[1]] + nums[2:], p2):
        return True
    if is_valid(target, [nums[0] * nums[1]] + nums[2:], p2):
        return True
    if p2 and is_valid(target, [int(str(nums[0]) + str(nums[1]))] + nums[2:], p2):
        return True
    return False

for line in D.strip().split('\n'):
    target, nums = line.strip().split(':')
    target = int(target)
    nums = [int(x) for x in nums.strip().split()]
    if is_valid(target, nums, p2=False):
        p1 += target
    if is_valid(target, nums, p2=True):
        p2 += target

print(p1)
print(p2)