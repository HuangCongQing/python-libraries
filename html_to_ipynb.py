'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-05-22 17:26:53
LastEditTime: 2021-05-22 17:27:27
FilePath: /python-libraries/html_to_ipynb.py
'''
from bs4 import BeautifulSoup
import json
import urllib.request

#  for local html file
response = open("/home/hcq/pointcloud/python-libraries/03Matplotlib/Python可视化Top50Matplotlib/week1 correlation live.html",encoding='utf8')
text = response.read()

soup = BeautifulSoup(text, 'lxml')
# see some of the html
print(soup.div)
dictionary = {'nbformat': 4, 'nbformat_minor': 1, 'cells': [], 'metadata': {}}
for d in soup.findAll("div"):
    if 'class' in d.attrs.keys():
        for clas in d.attrs["class"]:
            if clas in ["text_cell_render", "input_area"]:
                # code cell
                if clas == "input_area":
                    cell = {}
                    cell['metadata'] = {}
                    cell['outputs'] = []
                    cell['source'] = [d.get_text()]
                    cell['execution_count'] = None
                    cell['cell_type'] = 'code'
                    dictionary['cells'].append(cell)

                else:
                    cell = {}
                    cell['metadata'] = {}

                    cell['source'] = [d.decode_contents()]
                    cell['cell_type'] = 'markdown'
                    dictionary['cells'].append(cell)
open('/home/hcq/pointcloud/python-libraries/03Matplotlib/Python可视化Top50Matplotlib/week1 correlation live.ipynb', 'w').write(json.dumps(dictionary))
response.close()
