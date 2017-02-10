from urllib import urlopen
from link_finder import LinkFinder
from general import *
import os


class Spider:
    """
    Spider class containing class variables:
    """
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = os.path.join(Spider.project_name, 'queue.txt')
        Spider.crawled_file = os.path.join(Spider.project_name, 'crawled.txt')
        self.boot()
        self.crawl_page('First spider', Spider.base_url)

    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print "[*] {0} now crawling {1}".format(thread_name, page_url)
            print "[*] Queue {0} | Crawled: {1}".format(str(len(Spider.queue)), str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    @staticmethod
    def gather_links(page_url):
        """
        gather links from a given page url
        :param page_url:
        :return: set of links
        """
        html_string = ''
        try:
            response = urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html':
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)

        except Exception as e:
            print "[*] Error: can not crawl page"
            return set()

        finally:
            return finder.page_links()



    def add_links_to_queue(self,links):
        for url in links:
            if self.url_need_to_be_crawled(url):
                Spider.queue.add(url)


    def url_need_to_be_crawled(self, url):
        if url in Spider.queue:
            return False
        if url in Spider.crawled:
            return False
        if Spider.domain_name not in url:
            return False
        return True

    @staticmethod
    def update_files():
        set_to_file(Spider.queue,Spider.queue_file)
        set_to_file(Spider.crawled,Spider.crawled_file)