from tld import get_tld

def get_domain(url):
    res = get_tld(url, as_object=True)
    return res.fld

print get_domain("http://www.google.com")