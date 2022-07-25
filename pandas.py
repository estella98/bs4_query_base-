import requests
import re
import json
from bs4 import BeautifulSoup
url_list = ["https://pandas.pydata.org/docs/reference/io.html"
,"https://pandas.pydata.org/docs/reference/general_functions.html",
"https://pandas.pydata.org/docs/reference/series.html",
"https://pandas.pydata.org/docs/reference/frame.html",
"https://pandas.pydata.org/docs/reference/arrays.html",
"https://pandas.pydata.org/docs/reference/indexing.html",
"https://pandas.pydata.org/docs/reference/offset_frequency.html",
"https://pandas.pydata.org/docs/reference/window.html",
"https://pandas.pydata.org/docs/reference/groupby.html",
"https://pandas.pydata.org/docs/reference/resampling.html",
"https://pandas.pydata.org/docs/reference/style.html",
"https://pandas.pydata.org/docs/reference/plotting.html",
"https://pandas.pydata.org/docs/reference/general_utility_functions.html",
"https://pandas.pydata.org/docs/reference/extensions.html"]
my_dict = dict()
for base_url in url_list:
    print(f"processing base url{base_url}")
    page = requests.get(base_url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("tbody")
    for r in results:
        #print(r, "\n")
        title_r = r.find_all('tr')
        #print(f"11{title_r}\n")
        for _tr in title_r:
            if "title" not in _tr.a.attrs:
                #unexpected format
                continue
            print(f"the function title is: { _tr.a['title']}\n")
            func_name = _tr.a['title']
            print(f"the function description is: {_tr.find_all('p')[1]}")
            func_desc_raw = str(_tr.find_all('p')[1])
            func_desc_raw = func_desc_raw.lstrip('<p>')
            func_desc = func_desc_raw.rstrip('</p>')
            func_name_args = func_name.split(".")
           

            for i in range(len(func_name_args)-1, -1, -1):
                k = ".".join(func_name_args[i:])
                if k in my_dict:
                    if func_desc not in my_dict[k]:
                        my_dict[k].append(func_desc)
                else:
                    my_dict[k] = [func_desc]
            
                  

with open('result.json', 'w') as fp:
    
    json.dump(my_dict, fp)
