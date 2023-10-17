"""
FCFS is the simplest disk scheduling algorithm. As the name suggests, 
this algorithm entertains requests in the order they arrive in the disk queue.
 The algorithm looks very fair and there is no starvation (all requests are serviced sequentially) but generally, it does not provide the fastest service.

Algorithm: 

    1. Let Request array represents an array storing indexes of tracks that have been requested in ascending order of their time of arrival.
    ‘head’ is the position of disk head.
    2. Let us one by one take the tracks in default order and calculate the absolute distance of the track from the head.
    3. Increment the total seek count with this distance.
    4. Currently serviced track position now becomes the new head position.
    5. Go to step 2 until all tracks in request array have not been serviced.

"""

 
def FCFS(arr, head):
 
    seek_count = 0;
    distance, cur_track = 0, 0;
 
    for i in range(len(arr)):
        cur_track = arr[i];
 
        # calculate absolute distance
        distance = abs(cur_track - head);
 
        # increase the total count
        seek_count += distance;
 
        # accessed track is now new head
        head = cur_track;
     
    return seek_count,arr
     

