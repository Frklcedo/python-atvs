import time
import threading

start = time.perf_counter()


def fuck_you(name="Salazar"):
    print("fuck you")
    time.sleep(2)
    print(name)


t1 = threading.Thread(target=fuck_you)
t2 = threading.Thread(target=fuck_you)

t1.start()
t2.start()

finish = time.perf_counter()

t1.join()
t2.join()

print(finish - start, "fucks")
