import threading


class TestAndSetLock:
    def __init__(self):
        self.state = False

    def test_and_set(self):
        old_value = self.state
        self.state = True
        return old_value

    def release(self):
        self.state = False


buffer = []
buffer_size = 10
mutex = TestAndSetLock()
full = threading.Semaphore(0)
empty = threading.Semaphore(buffer_size)
result3=[]

def producer():
    global buffer
    while True:
        item = produce_item()
        empty.acquire()
        while mutex.test_and_set():
            pass
        print("Producer locked the mutex")
        buffer.append(item)
        mutex.release()
        print("Producer released the mutex")
        full.release()


def consumer():
    global buffer
    while True:
        full.acquire()
        while mutex.test_and_set():
            pass
        print("Consumer locked the mutex")
        item = buffer.pop(0)
        mutex.release()
        print("Consumer released the mutex")
        empty.release()
        consume_item(item)


def produce_item():
    return 1  # Placeholder for actual item production


def consume_item(item):
    pass  # Placeholder for actual item consumption


# Start the producer and consumer threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)
producer_thread.start()
consumer_thread.start()
