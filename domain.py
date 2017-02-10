from urlparse import *

def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')[-2:]
        return '.'.join(results)
    except Exception:
        return ''

def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except Exception:
        return ''
