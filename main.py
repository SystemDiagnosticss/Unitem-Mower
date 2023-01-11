import threading
import queue
import time
import cv2
from source.source import Source

ROWS = 1024
COLS = 768
CHANNELS = 3
FRAMES = 100
DECREASER = 2
KERNEL = 5
DIR = "./processed"

counter = FRAMES


def img_saver(queue):
    for i in range(queue.qsize()):
        cv2.imwrite(DIR + "/" + str(i) + ".png", queue.get())


def img_operation(img):
    img = cv2.resize(img, (int(img.shape[0] / DECREASER), int(img.shape[1] / DECREASER)))
    img = cv2.medianBlur(img, KERNEL)
    return img


def producer(img_creator, queue_a, counter):
    while counter >= 0:
        queue_a.put(img_creator.get_data())
        time.sleep(0.05)
        counter -= 1


def consumer(queue_a, queue_b):
    while True:
        try:
            img = None
            if queue_a.qsize():
                img = queue_a.get_nowait()
            if img is not None:
                img = img_operation(img)
                queue_b.put_nowait(img)
        except:
            break


def main():
    img_creator = Source((ROWS, COLS, CHANNELS))

    queue_a = queue.Queue(maxsize=counter)
    queue_b = queue.Queue(maxsize=counter)

    prod_t = threading.Thread(target=producer, args=(img_creator, queue_a, counter))
    cons_t = threading.Thread(target=consumer, args=(queue_a, queue_b))

    prod_t.start()
    cons_t.start()

    prod_t.join()
    cons_t.join()

    img_saver(queue_b)


if __name__ == "__main__":
    main()
