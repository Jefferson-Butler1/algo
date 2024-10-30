def matchRegion(pattern, region, x, y):
    m = len(pattern)
    if y + len(pattern) > len(region):
        return False
    if x + len(pattern) > len(region):
        return False
    for i in range(m):
        for ii in range(m):
            if pattern[i][ii] != region[x + i][y + ii]:
                return False
   # print("Returns")
   # for row in pattern:
   #     print(row)
   # for row in [[a for a in row[x : x + m]] for row in region[y : y + m]]:
   #     print(row)
    return True


def match(pattern, text):
   # for row in pattern:
   #     print(row)
   # for row in text:
   #     print(row)
   # # only checks top left of pattern
    for i in range(len(text)):
        for ii in range(len(text)):
            if matchRegion(pattern, text, i, ii):
                return (i, ii)
    return None


text = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
pattern = [[5,6],[8,9]]

print(match(pattern, text))
