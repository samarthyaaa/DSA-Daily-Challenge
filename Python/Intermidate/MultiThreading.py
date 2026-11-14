from threading import Thread

def square_numbers():
    for i in range(100):
        i*i

if __name__ == '__main__':
    threads=[]
    nums_threads=10

    # to create threads
    for i in range(nums_threads):
        thread = Thread(target=square_numbers)
        threads.append(thread)
    # to start threads
    for thread in threads:
        thread.start()
    # to join threads: wait for them to complete
    for thread in threads:
        thread.join()
    print("End Main")
