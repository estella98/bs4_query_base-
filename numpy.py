import requests
import re
import json
from bs4 import BeautifulSoup
base_url = "https://numpy.org/devdocs/reference/generated/numpy.ndarray.all.html"
root_url = "https://numpy.org/devdocs/reference/generated/"

my_dict = dict()
def extract_all_urls(base_url):
    url_list = []
    page = requests.get(base_url)
    soup = BeautifulSoup(page.content, "html.parser")
    urls = soup.find_all('li')
    print(urls)
    for res in urls:
        print(f"14{res}")
        if str(res.a["href"]).startswith("numpy"):
            url_list.append(root_url + res.a["href"])
    print(url_list)
    return url_list[1:]

def extract_single(base_url, p_idx = 1):
    print(base_url)
    page = requests.get(base_url)
    soup = BeautifulSoup(page.content, "html.parser")
    func_name = str(soup.find_all('h1')[0])
    func_name = re.search('<h1>(.+?)<', func_name).group(1)
  # print(f"**********{soup.find_all('p')}")
    func_desc = str(soup.find_all('p')[p_idx])
    if not re.search('<p>(.+?)</p>', func_desc):
        print(f"skip {func_desc}")
        return
    func_desc = re.search('<p>(.+?)</p>', func_desc).group(1)
    print(f"{func_name}:{func_desc}")
    my_dict[func_name] = func_desc



#extract ndarray func
nd_html = "https://numpy.org/devdocs/reference/generated/numpy.ndarray.all.html"
nd_array_url_list = extract_all_urls(nd_html)
for url in nd_array_url_list:
    extract_single(url)

#extract scalar func
scalar_html = "https://numpy.org/devdocs/reference/generated/numpy.generic.flags.html"
scalar_url_list = extract_all_urls(scalar_html)
for url in scalar_url_list:
    extract_single(url)

#extract dtype func
dtype_html = "https://numpy.org/devdocs/reference/generated/numpy.dtype.type.html"
dtype_url_list = extract_all_urls(dtype_html)
for url in dtype_url_list:
    extract_single(url)

#extract routine func
routine_html = "https://numpy.org/devdocs/reference/generated/numpy.empty.html"
routine_list = extract_all_urls(routine_html)
for url in routine_list:
    extract_single(url, 0)

#extract array manipulation routines func
array_routine_html = "https://numpy.org/devdocs/reference/generated/numpy.shape.html"
arr_routine_list =  extract_all_urls(array_routine_html)
for url in arr_routine_list:
    extract_single(url, 0)

#extract binary op
binary_op_html = "https://numpy.org/devdocs/reference/generated/numpy.bitwise_and.html"
binary_op_list =  extract_all_urls(binary_op_html )
for url in binary_op_list:
    extract_single(url, 0)

#extract string op
string_op_html = "https://numpy.org/devdocs/reference/generated/numpy.char.add.html"
string_op_list = extract_all_urls(string_op_html)
for url in string_op_list:
    extract_single(url, 0)

#datetime op
datetime_op_html = "https://numpy.org/devdocs/reference/generated/numpy.datetime_as_string.html"
datetime_op_list = extract_all_urls(datetime_op_html)
for url in datetime_op_list:
    extract_single(url, 0)

#datatype routines
datatype_op_html = "https://numpy.org/devdocs/reference/generated/numpy.promote_types.html"
datatype_op_list = extract_all_urls(datatype_op_html)
for url in datatype_op_list:
    extract_single(url, 0)

#fft
fft_html = "https://numpy.org/devdocs/reference/generated/numpy.fft.fft.html"
fft_op_list = extract_all_urls(fft_html)
for url in fft_op_list:
    extract_single(url, 0)

#io
io_html = "https://numpy.org/devdocs/reference/generated/numpy.save.html"
io_list = extract_all_urls(io_html)
for url in io_list:
    extract_single(url, 0)

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
    




