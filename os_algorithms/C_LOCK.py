def c_lock(arr, head):
    # sort the requests
    sorted_arr = sorted(arr)

    # divide the requests into two sub-lists
    right = [x for x in sorted_arr if x >= head]
    left = [x for x in sorted_arr if x < head]

    # concatenate the two sub-lists
    ordered = right + left

    # calculate the total seek count
    seek_count = sum([abs(ordered[i] - ordered[i-1]) for i in range(1, len(ordered))])

    # return the seek count and the ordered sequence
    return seek_count, ordered
