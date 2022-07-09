#!/usr/bin/env python
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from pprint import pprint

if __name__ == "__main__":
    env = Environment(undefined=StrictUndefined)
    env.loader = FileSystemLoader("./templates/")

    template_file = "vrf_definition.j2"

    vars=[
    {
    'vrf_name': 'blue',
    'rd_number': '100:100',
    'ipv4_enabled': True,
    'ipv6_enabled': True,
    },
    {
   'vrf_name': 'red',
   'rd_number': '200:200',
   'ipv4_enabled': True,
   'ipv6_enabled': True,
    },
    {
    'vrf_name': 'orange',
    'rd_number': '300:300',
    'ipv4_enabled': True,
    'ipv6_enabled': True,
    },
    { 
    'vrf_name': 'purple',
    'rd_number': '400:400',
    'ipv4_enabled': True,
    'ipv6_enabled': True,
    },    
    ] 
    print()
    template = env.get_template(template_file)
    for vrf in vars:
      cfg = template.render(**vrf)
      print(cfg)
 
