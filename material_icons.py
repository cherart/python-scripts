import requests
import json
from bs4 import BeautifulSoup

icon_dict = {}
icons = []

url = 'https://github.com/google/material-design-icons/tree/master/action/svg/design'
r = requests.get(url)
soup = BeautifulSoup(r.text)
icon_names = soup.select("tr.js-navigation-item td.content .css-truncate a")
for i in icon_names:
    name = i.contents[0]
    index_first_underscore = name.index('_')
    index_last_underscore = name.rindex('_')
    icon_name = name[index_first_underscore+1:index_last_underscore]
    icons.append(icon_name)
unique_icons_list = list(set(icons))
icon_dict['design'] = unique_icons_list
j = json.dumps(icon_dict, indent=4)
f = open('icons.json', 'w')
print >> f, j
# python3 print (j, file=f)
f.close()
