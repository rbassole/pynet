#!/usr/bin/env python

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('./templates/')

nxos1 = {'intf':'Ethernet1/1','ip_addr': '1.1.100.1','mask': 24,'local_as': 22}
nxos2 = {'intf':'Ethernet1/1','ip_addr': '1.1.100.2','mask': 24,'local_as': 22}

for device in (nxos1, nxos2):
  template_file = 'nxos_intf.j2'
  template = env.get_template(template_file)
  output = template.render(**device)
  print(output)

