
def c_scan(arr, head,disk_size):
    # sort the requests
    sorted_arr = sorted(arr)

    # divide the requests into two sub-lists
    right = [x for x in sorted_arr if x > head] + [disk_size - 1]
    left = [0] + [x for x in sorted_arr if x <= head]

    # concatenate the two sub-lists
    ordered = right + left
    print(left)
    print(right)
    print(ordered)
    # calculate the total seek count
    seek_count = sum([abs(ordered[i] - ordered[i-1]) for i in range(1, len(ordered))])

    # return the seek count and the ordered sequence
    return seek_count, ordered

c_scan([110,30,4,11,33,55,60,7],50,200)
