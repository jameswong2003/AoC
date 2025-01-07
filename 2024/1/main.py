with open("data.txt") as f:
    lines = f.read().splitlines()

left = []
right = []

for line in lines:
    x, y = line.split()
    left.append(int(x))
    right.append(int(y))

def part_one(left, right):
    sorted_left, sorted_right = sorted(left), sorted(right)
    res = 0
    for i in range(len(sorted_left)):
        res += abs(sorted_left[i] - sorted_right[i])
    
    return res

def part_two(left, right):
    count = {}
    for n in left:
        count[n] = 0
    
    for n in right:
        if n in count:
            count[n] += 1

    res = 0
    for key, value in count.items():
        res += key * value
    return res

print(part_two(left, right))