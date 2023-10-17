import threading

# List of books
books = {
    "Book 1": {"reserved": False, "reserved_by": None},
    "Book 2": {"reserved": False, "reserved_by": None},
    "Book 3": {"reserved": False, "reserved_by": None},
    "Book 4": {"reserved": False, "reserved_by": None},
    "Book 5": {"reserved": False, "reserved_by": None}
}

# Counter for the number of readers
readers = 0

# Mutex lock for the readers counter
readers_lock = threading.Lock()

# Mutex lock for reserving a book
reserve_lock = threading.Lock()

def reserve_book(book, reader_id):
    global readers

    # Acquire the readers lock to increment the readers counter
    with readers_lock:
        readers += 1
        if readers == 1:
            # If this is the first reader, acquire the reserve lock to prevent writers from accessing the books
            reserve_lock.acquire()

    # Check if the book is available
    if not books[book]["reserved"]:
        # Reserve the book for the reader
        books[book]["reserved"] = True
        books[book]["reserved_by"] = reader_id
        print(f"Book '{book}' is reserved by reader {reader_id}")
    else:
        print(f"Book '{book}' is already reserved by reader {books[book]['reserved_by']}")

    # Release the readers lock to decrement the readers counter
    with readers_lock:
        readers -= 1
        if readers == 0:
            # If this is the last reader, release the reserve lock to allow writers to access the books
            reserve_lock.release()

def return_book(book):
    # Return the book to the library
    books[book]["reserved"] = False
    books[book]["reserved_by"] = None
    print(f"Book '{book}' is returned to the library")

def main():
    # Create multiple threads for readers and writers
    threads = []
    for i in range(10):
        if i % 2 == 0:
            # Half of the threads are readers
            threads.append(threading.Thread(target=reserve_book, args=(f"Book {(i // 2) + 1}", i)))
        else:
            # Half of the threads are writers
            threads.append(threading.Thread(target=return_book, args=(f"Book {(i // 2) + 1}",)))

    # Start the threads
    for thread in threads:
        thread.start()

    # Wait for the threads to finish
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()
