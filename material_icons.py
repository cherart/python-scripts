import requests
import json
from bs4 import BeautifulSoup

icon_dict = {}
icons = []
cats = []
urls = []
version = 'master'
html_output = ''

# get icon categories from folder names from github

def getIconCats():
    url = 'https://github.com/google/material-design-icons/tree/{0}/'.format(version)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    all_names = soup.select("tr.js-navigation-item td.content .css-truncate a")
    for i in all_names:
        if 'tree' in i.attrs[u'href']:
            cat = i.contents[0]
            if cat != 'sprites':
                cats.append(cat)
    return cats

html_output += '<div class="container">'
# create dictionary with all icon names (verbose)
for cat in getIconCats():
    url = 'https://github.com/google/material-design-icons/tree/{0}/{1}/svg/design'.format(version, cat)
    r = requests.get(url)
    print ('.')
    soup = BeautifulSoup(r.text, "html.parser")
    icon_names = soup.select("tr.js-navigation-item td.content .css-truncate a")
    # get icon name from svg filename
    for i in icon_names:
        name = i.contents[0]
        index_first_underscore = name.index('_')
        index_last_underscore = name.rindex('_')
        icon_name = name[index_first_underscore+1:index_last_underscore]
        icons.append(icon_name)
    unique_icons_list = list(set(icons))
    for icon in unique_icons_list:
        html_output += '<span class="badge badge-info"><i class="material-icons" style="vertical-align: middle">{0}</i> {0}</span> &nbsp;'.format(icon)
    icon_dict[cat] = unique_icons_list
html_output += '</div>'

# generate json output file
j = json.dumps(icon_dict, indent=4)
f = open('icons.json', 'w')
print >> f, j
# python3 print (j, file=f)
f.close()

# generate html output file
# import webbrowser
f = open('icons.html', 'w')
html = '<html><head><meta charset="utf-8">'\
    '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">'\
    '<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">' \
    '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.2/css/bootstrap.min.css">'\
    '</head>' \
    '<body><h1>Material Icons</h1>{0}</body></html>'.format(html_output)
f.write(html)
f.close()
# webbrowser.open_new_tab('icons.html')
