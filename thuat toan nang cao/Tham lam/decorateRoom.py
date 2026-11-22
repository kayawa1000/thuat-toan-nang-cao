def decorateRoom(r, g, b):
    colors = sorted([r, g, b])
    two_smallest = colors[0] + colors[1]
    total_div_3 = (r + g + b) // 3
    return min(two_smallest, total_div_3)
