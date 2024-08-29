def hurdleRace(k, height):
    maxHeight = max(height)

    if k >= maxHeight:
        return 0
    else:
        return maxHeight - k

print(hurdleRace(
    4,
    [1, 6, 3, 2]
) == 2)
print(hurdleRace(
    7,
    [2, 5, 4, 5, 2]
) == 0)