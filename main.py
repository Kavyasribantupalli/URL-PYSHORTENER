import pyshorteners
def url_shortener(url):
    urlshortener=pyshorteners.Shortener()
    a=urlshortener.tinyurl.short(url)
    return a
url=input("Enter the url:")
print(url_shortener(url))

