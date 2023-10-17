def shortest_seek_time_first(requests, head,disk_size):
    seek_count = 0
    seek_sequence = [head]
    while len(requests) > 0:
        diff = [abs(request - head) for request in requests]
        index = diff.index(min(diff))
        seek_count += diff[index]
        head = requests[index]
        seek_sequence.append(head)
        requests.pop(index)
    return seek_count, seek_sequence
    
