
"""Same algorithm of scan but 0 doesn't included"""
def LOCK(arr, head, direction):
    seek_count = 0
    left = [] if direction == "left" else []
    right = [] if direction == "right" else []
    for i in arr:
        if i < head:
            left.append(i)
        elif i > head:
            right.append(i)
    left.sort(reverse=True)
    right.sort()
    seek_sequence = []
    for _ in range(2):
        if direction == "left":
            for i in left:
                seek_sequence.append(i)
                seek_count += abs(head - i)
                head = i
            direction = "right"
        else:
            for i in right:
                seek_sequence.append(i)
                seek_count += abs(head - i)
                head = i
            direction = "left"
    return seek_count,seek_sequence