#!/usr/bin/env python
import json
from pprint import pprint

my_dict={}

with open('j_arp.json', 'r') as f:
    output =json.load(f)

length=len(output['ipV4Neighbors'])

for i in range(length):
    my_dict[output['ipV4Neighbors'][i]['address']] = output['ipV4Neighbors'][i]['hwAddress']

pprint(my_dict)
