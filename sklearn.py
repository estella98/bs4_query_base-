import requests
import re
import json
from bs4 import BeautifulSoup
url = "https://scikit-learn.org/stable/modules/classes.html#sklearn-metrics-metrics"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all("tbody")
my_dict = dict()
for r in results:
    td = r.find_all('td')
    func_name = ""
    func_descrip = ""
    for _td in td:
            if _td.a:
                func_name  = (_td.a.get('title'))
            else:
                func_descrip = (_td.p.get_text())
                my_dict[func_name] = func_descrip
print(my_dict)
data = dict()
with open('result.json', 'r') as fp:
    data = json.load(fp)
    for k,v in my_dict.items():
        func_name_args = k.split(".")
        for i in range(len(func_name_args)-1, -1, -1):
                k = ".".join(func_name_args[i:])
                if k in data:
                    if v not in data[k]:
                        data[k].append(v)
                else:
                    data[k] = [v]
        
      
with open('result.json', 'w') as fp:
    json.dump(data, fp)
    




