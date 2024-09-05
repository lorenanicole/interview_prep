import string

def designerPdfViewer(h, word):
    # h is always 1 <= h <= 7
    # word max len is 10
    # all lets are 1mm
    # a at indx 0, z at indx 25
    letters = string.ascii_lowercase
    maxHeight, numChars = 0, 0
    for char in word:
        if not char.isalpha():
            continue
        numChars += 1
        charIndx = letters.index(char)
        if h[charIndx] > maxHeight:
            maxHeight = h[charIndx]

    return maxHeight * 1 * numChars


print(designerPdfViewer(
    [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    'abc'
) == 9)
print(designerPdfViewer(
    [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7],
    'zaba'
) == 28)
print(designerPdfViewer(
    [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 1, 1, 5, 5, 1, 5, 2, 5, 5, 5, 5, 5, 5],
    ' torn'
) == 8)