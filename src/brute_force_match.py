def matchRegion(pattern, region, x, y):
    for i in range(len(pattern)):
        for ii in range(len(pattern[0])):
            if pattern[i][ii] != region[x+i][y+ii]:
                return False
    return True


def match(pattern, text):
    for row in pattern:
        print(row)
    for row in text:
        print(row)
    # only checks top left of pattern
    for i in range(len(text)):
        for ii in range(len(text[0])):
            if matchRegion(pattern, text, i, ii):
                return (i, ii)
