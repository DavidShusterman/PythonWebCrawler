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


print get_domain_name(r'https://www.google.co.il/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=python%20class%20variable')