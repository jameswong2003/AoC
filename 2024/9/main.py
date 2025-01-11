infile = 'data.txt'
D = open(infile).read().strip()

res = []
id = 0
idx = 0
while idx < len(D):
    if idx == len(D) - 1:
        res += [str(id)] * int(D[idx])
        break

    if idx % 2 == 0:
        res += [str(id)] * int(D[idx])
        id += 1
    else:
        res += '.' * int(D[idx])
    
    idx += 1

l, r = 0, len(res) - 1
while l < len(res) and l < r:
    if res[l] == '.':
        while res[r] == '.':
            r -= 1
        
        res[l] = res[r]
        res[r] = '.'
    l += 1

p1 = 0
for i in range(len(res)):
    p1 += int(res[i]) * i if res[i] != '.' else 0
print(p1)