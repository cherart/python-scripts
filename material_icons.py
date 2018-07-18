import requests
import json
from bs4 import BeautifulSoup

icon_dict = {}
cats = []
html_output = ''
count = 0

version = 'master'
base_url = 'https://github.com/google/material-design-icons/tree/{0}/'.format(version)

# get icon categories from folder names from github

def getIconCats():
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text, "html.parser")
    all_names = soup.select("tr.js-navigation-item td.content .css-truncate a")
    for i in all_names:
        if 'tree' in i.attrs[u'href']:
            cat = i.contents[0]
            if cat not in ['sprites', 'iconfont']:
                cats.append(cat)
    return cats

html_output += '<div class="container">'

# create dictionary with all icon names (verbose)
icon_cats = getIconCats()
for cat in icon_cats:
    icons = []
    unique_icons_list = []
    count +=1
    percent_done = round((float(count)/len(icon_cats))*100, 2)
    print ('{0} % done'.format(percent_done))
    html_output += '<h2>' + cat + '</h2>'

    url = '{0}{1}/svg/design'.format(base_url, cat)
    print url
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    icon_names = soup.select("tr.js-navigation-item td.content .css-truncate a")

    # get icon name from svg filename
    for i in icon_names:
        name = i.contents[0]
        index_first_underscore = name.index('_')
        index_last_underscore = name.rindex('_')
        icon_name = name[index_first_underscore+1:index_last_underscore]
        icons.append(icon_name)

    # icons list per cat
    unique_icons_list = list(set(icons))
    icon_dict[cat] = unique_icons_list

    # html output
    for icon in unique_icons_list:
        html_output += '<span class="badge badge-info" style="margin-bottom: .5em">' \
            '<i class="material-icons" style="vertical-align: middle">{0}</i> {0}</span> &nbsp;'.format(icon)

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
