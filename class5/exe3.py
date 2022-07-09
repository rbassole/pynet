#!/usr/bin/env python
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

if __name__ == "__main__":
    env = Environment(undefined=StrictUndefined)
    env.loader = FileSystemLoader("./templates/")

    template_file = "vrf_definition.j2"

    vars={
    'ipv4_enabled': True,
    'ipv6_enabled': True,
    'vrf_name': 'blue',
    'rd_number': '100:100'
    }
   
    print()
    template = env.get_template(template_file)
    cfg = template.render(**vars)
    print(cfg)
 
