#! /usr/bin/env python

from netmiko import ConnectHandler
from pprint import pprint
from datetime import datetime

cisco4 ={
 'device_type': 'cisco_nxos',
 'host': 'cisco4.lasthop.io',
 'username': 'pyclass',
 'password': '88newclass',
 'global_delay_factor': 2
}

start_time=datetime.now()
with ConnectHandler(**cisco4) as conn:
  output = conn.send_command('show version', use_textfsm=True)
  output += conn.send_command('show lldp neighbors', use_textfsm=True)
  end_time = datetime.now()
  pprint (output)
  print (f"Interface {output[1]['neighbor_interface']} on HPE is used to connect router Cisco4")
print(end_time - start_time)
