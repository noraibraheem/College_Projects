import threading
import time
import random

BUFFER_SIZE = 10
buffer = []
lock = threading.Lock()
full = threading.Semaphore(0)
empty = threading.Semaphore(BUFFER_SIZE)
result3 = []

class ProducerThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.item = None
        self.buffer = None

    def run(self):
        global buffer
        count = 0
        while count < 5:
            item = random.randint(1, 100)
            empty.acquire()
            lock.acquire()
            buffer.append(item)
            count += 1
            self.item = item
            self.buffer = buffer
            result3.append(f"Produced {item}. Buffer: {buffer}")  # Append to result3 list
            lock.release()
            full.release()
            time.sleep(random.randint(1, 3))


class ConsumerThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.item = None
        self.buffer = None

    def run(self):
        global buffer
        count = 0
        while count < 5:
            full.acquire()
            lock.acquire()
            item = buffer.pop(0)
            count += 1
            self.item = item
            self.buffer = buffer
            result3.append(f"Consumed {item}. Buffer: {buffer}")  # Append to result3 list
            lock.release()
            empty.release()
            time.sleep(random.randint(1, 3))


