with open("data.txt", "r") as file:
    input_data = file.readlines()
    input_data = [list(line.strip()) for line in input_data]

def part_one(input):
    word = 'XMAS'
    
    def is_word_in_direction(i, j, di, dj, input):
        word = ''
        for c in range(4):  # 4 to include current position + 3 more cells
            ni, nj = i + di * c, j + dj * c
            if not (0 <= ni < len(input) and 0 <= nj < len(input[0])): 
                return False
            word += input[ni][nj]
        return word == 'XMAS'
    
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),  # top, bottom, left, right
        (-1, -1), (-1, 1), (1, -1), (1, 1)  # top-left, top-right, bottom-left, bottom-right
    ]
    
    res = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 'X':
                for di, dj in directions:
                    if is_word_in_direction(i, j, di, dj, input):
                        res += 1
    return res

def part_two(input):
    def valid_xmas(i, j, input):
        if i - 1 < 0 or i + 1 >= len(input) or j - 1 < 0 or j + 1 >= len(input[0]):
            return False
        
        s1 = set(['M', 'S'])
        s1.discard(input[i - 1][j - 1])
        s1.discard(input[i + 1][j + 1])

        s2 = set(['M', 'S'])
        s2.discard(input[i - 1][j + 1])
        s2.discard(input[i + 1][j - 1])

        return len(s1) == 0 and len(s2) == 0
    
    res = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 'A':
                res += 1 if valid_xmas(i, j, input) else 0
    return res

print(part_two(input_data))
