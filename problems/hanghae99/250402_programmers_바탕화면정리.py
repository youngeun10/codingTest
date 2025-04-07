def solution(wallpaper):
    x = []
    y = []

    for i, r in enumerate(wallpaper):
        for j, c in enumerate(wallpaper[i]):
            if c == '#':
                x.append(i)
                y.append(j)

    return [min(x), min(y), max(x)+1, max(y)+1]