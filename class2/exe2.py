#! /usr/bin/env python

from netmiko import ConnectHandler
from pprint import pprint
from datetime import datetime

nxos2 ={
 'device_type': 'cisco_nxos',
 'host': 'nxos2.lasthop.io',
 'username': 'pyclass',
 'password': '88newclass',
 'global_delay_factor': 2
}

start_time=datetime.now()
with ConnectHandler(**nxos2) as conn:
 #output = conn.send_command('show lldp neighbors detail, delay_factor=8, fast_cli=False)
  output = conn.send_command('show lldp neighbors detail')
  end_time = datetime.now()
  print (output)
print(end_time - start_time)
