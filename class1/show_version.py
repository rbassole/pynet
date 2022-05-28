#! /usr/bin/env python

from netmiko import ConnectHandler

device = {
  'device_type': 'cisco_ios',
  'host': 'cisco3.lasthop.io',
  'username': 'pyclass',
  'password': '88newclass',
}

con = ConnectHandler (**device)

output = con.send_command('show version')

with open('show_version.txt','w') as f:
  f.write(output)
