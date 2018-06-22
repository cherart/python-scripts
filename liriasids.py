import requests

urls = []
newids = []


def getNewLiriasId(url):
    r = requests.get(url)
    if r.history:
        if 'docid' in r.url:
            afterdocid = r.url.split("docid=", 1)[1]
            newid = afterdocid.split("&", 1)[0]
            # print newid
            return newid
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
    newids.append(newid)
print ','.join(newids)
