import threading
import Queue
from spider import Spider
from domain import *
from general import *
import os

PROJECT_NAME = 'thenewboston'
HOMEPAGE = 'https://thenewboston.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = os.path.join(PROJECT_NAME, 'queue.txt')
CRAWLER_FILE = os.path.join(PROJECT_NAME, 'crawler.txt')
NUMBER_OF_THREADS = 4
queue = Queue.Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


def create_spiders():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name,url)
        queue.task_done()


def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print "[*] {0} links in the queue".format(str(queued_links))
        create_jobs()



create_spiders()
crawl()


if __name__ == '__main__':
    main()
