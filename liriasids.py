import requests
# from urlparse import urlparse

urls = []
newids = []


def getNewLiriasId(url):
    r = requests.get(url)
    if r.history:
        if 'docid' in r.url:
            return r.url.split("docid=", 1)[1].split("&", 1)[0]
            #  parsedurl = urlparse(r.url)
            #  return parsedurl.query.split("&")[0][6:]
        else:
            print "No new id found for {0}".format(url)
            return ''
    else:
        print "Request was not redirected. No new id found for {0}".format(url)


input = raw_input("Old lirias id:")
oldids = input.replace(" ", "").split(",")
for oldid in oldids:
    urls.append('https://lirias.kuleuven.be/handle/123456789/{0}'.format(oldid))
for url in urls:
    newid = getNewLiriasId(url)
    if newid != '':
        newids.append(newid)
print ','.join(newids)
