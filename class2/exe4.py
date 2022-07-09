#! /usr/bin/env python

from netmiko import ConnectHandler
from pprint import pprint
from datetime import datetime

cisco3 ={
 'device_type': 'cisco_nxos',
 'host': 'cisco3.lasthop.io',
 'username': 'pyclass',
 'password': '88newclass',
 'fast_cli': True 
}
cmd=['ip name-server 1.1.1.1', 'ip name-server 1.0.0.1', 'ip domain-lookup']
start_time=datetime.now()
with ConnectHandler(**cisco3) as conn:
  output = conn.send_config_set(cmd)
  output += conn.send_command('ping google.com', strip_prompt=False, strip_command=False)
  end_time = datetime.now()
  print (output)
print(end_time - start_time)
