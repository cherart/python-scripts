# Readme for python scripts

## requirements and usage

Base setup need to run these scripts
use pip to install this in your virtualenv before running the script

```console
(tplone)
bin/pip install [dependencies]
bin/python liriasids.py
```
dependecies per packages are indicated per script, install each of them seperately

## material icons

### dependencies

- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

### functionality

- This is a web scraping script that gets all the icons per category from the [Material Icons github repository](https://github.com/google/material-design-icons)
- Since it is not easily possible to get this list from the [Material Icons website](http://google.github.io/material-design-icons/), the list is not available in the source, or via a normal python request and it would require a lot of setup with selenium or phantomjs and I didn't want to go there, this is an alternative
- By default this is getting the info from the master branch, but you can change this by changing the version variable at the beginning of the script
- It will generate a json and html output file showing the icons per category

### example
to see the output, you can use the github html preview:
- http://htmlpreview.github.io/?https://github.com/spereverde/python-scripts/blob/master/icons.json
- http://htmlpreview.github.io/?https://github.com/spereverde/python-scripts/blob/master/icons.html

## liriasids.py

### dependencies

- [requests](https://pypi.org/project/requests/)

### functionality

* It will ask you for a (list of ) old lirias ids (can contain comma's and spaces)
* It will return a comma seperated list of the corresponding Lirias 2.0 ids
* It will notify you when one of the given ids has no new id

### example

```console
$ bin/python liriasids.py
Old lirias id:541287,594303,502935,583939,503805,495236,470495,356555,318542,284465,340170
LIRIAS1867197,LIRIAS1867573,LIRIAS1536116,LIRIAS1867518,LIRIAS475124,LIRIAS475126,LIRIAS1866946,LIRIAS1866372,LIRIAS1866169,LIRIAS1863378,LIRIAS1866319
```

