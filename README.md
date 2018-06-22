# Readme for python scripts

## liriasids.py

### requirements and usage

This script requires python [requests](https://pypi.org/project/requests/)
use pip to install this in your virtualenv before running the script

```console
(tplone)
bin/pip install requests
bin/python liriasids.py
```

### functionality

* It will ask you for a (list of ) old lirias ids (can contain comma's and spaces)
* It will return a comma seperated list of the corresponding Lirias 2.0 ids
* It will notify you when one ofd the given ids has no new id

### example

```console
$ bin/python liriasids.py
Old lirias id:541287,594303,502935,583939,503805,495236,470495,356555,318542,284465,340170
LIRIAS1867197,LIRIAS1867573,LIRIAS1536116,LIRIAS1867518,LIRIAS475124,LIRIAS475126,LIRIAS1866946,LIRIAS1866372,LIRIAS1866169,LIRIAS1863378,LIRIAS1866319
```

