from HTMLParser import *
from urlparse import *

WANTED_TAG = 'a'
WANTED_ATTRIBUTE = 'href'


class LinkFinder(HTMLParser):
    def __init__(self, base_url, page_url):
        HTMLParser.__init__(self)
        self.base_url_ = base_url
        self._page_url = page_url
        self._links = set()

    def handle_starttag(self, tag, attrs):
        if tag == WANTED_TAG:
            for (attribute, value) in attrs:
                if attribute == WANTED_ATTRIBUTE:
                    url = urljoin(self.base_url_, value)
                    self._links.add(url)

    def page_links(self):
        return self._links



