
"""Sure, here are the step-by-step instructions for the original algorithm:

1. Initialize `seek_count` to zero, and create empty lists `left`, `right`, and `seek_sequence`.
2. Append either the beginning or end of the disk (depending on the `direction`) to the corresponding list.
3. Sort the input request array into the `left` and `right` lists based on whether the track is less than or greater than the current head position.
4. Run a loop twice, first scanning the right side of the head, then reversing direction and scanning the left side:
	1. If the `direction` is "left", loop through the `left` list in reverse order:
		1. Set `cur_track` to the current track in the `left` list.
		2. Append `cur_track` to the `seek_sequence` list.
		3. Calculate the absolute distance between `cur_track` and `head`, and add it to `seek_count`.
		4. Update the `head` position to `cur_track`.
	2. If the `direction` is "right", loop through the `right` list:
		1. Set `cur_track` to the current track in the `right` list.
		2. Append `cur_track` to the `seek_sequence` list.
		3. Calculate the absolute distance between `cur_track` and `head`, and add it to `seek_count`.
		4. Update the `head` position to `cur_track`.
	3. Reverse the `direction` after the first loop.
5. Print out the total seek count and the seek sequence list."""



disk_size = 200

def SCAN(arr, head,disk_size, direction):
    seek_count = 0
    distance, cur_track = 0, 0
    left = []
    right = []
    seek_sequence = []
    
    if direction == "left":
        left.append(0)
    elif direction == "right":
        right.append(disk_size - 1)
    
    for i in range(len(arr)):
        if arr[i] < head:
            left.append(arr[i])
        if arr[i] > head:
            right.append(arr[i])
    
    left.sort()
    right.sort()
    
    run = 2
    while run != 0:
        if direction == "left":
            for i in range(len(left) - 1, -1, -1):
                cur_track = left[i]
                seek_sequence.append(cur_track)
                distance = abs(cur_track - head)
                seek_count += distance
                head = cur_track
            direction = "right"
        elif direction == "right":
            for i in range(len(right)):
                cur_track = right[i]
                seek_sequence.append(cur_track)
                distance = abs(cur_track - head)
                seek_count += distance
                head = cur_track
            direction = "left"
        run -= 1
    
    return seek_count,seek_sequence