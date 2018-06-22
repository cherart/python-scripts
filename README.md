# Readme for python scripts

## liriasids.py

### requirements and usage

This script requires python [requests](https://pypi.org/project/requests/)
use pip to install this in your virtualenv before running the script

~~~
(tplone)
bin/pip install requests
bin/python liriasids.py
~~~

### functionality

* It will ask you for a (list of ) old lirias ids (can contain comma's and spaces)
* It will return a comma seperated list of the corresponding Lirias 2.0 ids
* It will notify you when one ofd the given ids has no new id

