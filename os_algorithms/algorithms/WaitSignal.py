import threading
import time
import random

# define a shared buffer and its maximum size
buffer = []
max_size = 5

# create two event objects: one for the producer and one for the consumer
producer_event = threading.Event()
consumer_event = threading.Event()

# define a function to simulate the producer
def producer():
    global buffer
    print("Starting producer thread")
    for i in range(10):
        item = random.randint(1, 100)
        print(f"producer: generated item {item}")
        producer_event.wait()
        if len(buffer) < max_size:
            buffer.append(item)
            print(f"producer: added item {item} to buffer")
        else:
            print("producer: buffer is full, waiting for consumer")
            consumer_event.set()
            producer_event.clear()
        time.sleep(random.randint(1, 3))
    print("Ending producer thread")

# define a function to simulate the consumer
def consumer():
    global buffer
    print("Starting consumer thread")
    while True:
        consumer_event.wait()
        if len(buffer) > 0:
            item = buffer.pop(0)
            print(f"consumer: removed item {item} from buffer")
            producer_event.set()
            consumer_event.clear()
        else:
            print("consumer: buffer is empty, waiting for producer")
            producer_event.set()
            consumer_event.clear()
        time.sleep(random.randint(1, 3))
    print("Ending consumer thread")

# create the threads
t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

# start the threads
t1.start()
t2.start()

# signal the producer event to start the producer thread
print("Main thread: signaling producer to start")
producer_event.set()

# wait for the threads to finish
t1.join()
t2.join()

print("Main thread: all threads have finished")

# In this example, we have a shared buffer that can hold up to max_size items. The producer generates random items and adds them to the buffer, while the consumer removes items from the buffer. The two threads are coordinated using two Event objects: producer_event and consumer_event.

# The producer waits for the producer_event to be set before generating an item and attempting to add it to the buffer. If the buffer is full, the producer sets the consumer_event and clears the producer_event, indicating to the consumer thread that it should remove an item from the buffer. The producer then sleeps for a random amount of time before repeating the loop.

# Similarly, the consumer waits for the consumer_event to be set before attempting to remove an item from the buffer. If the buffer is empty, the consumer setsthe producer_event and clears the consumer_event, indicating to the producer thread that it should generate a new item and add it to the buffer. The consumer then sleeps for a random amount of time before repeating the loop.

# The main thread signals the producer_event to start the producer thread and waits for both threads to finish before printing a final message indicating that all threads have finished.