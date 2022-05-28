#! /usr/bin/env python

from netmiko import ConnectHandler

list_nxos = [{
 'device_type': 'cisco_nxos',
 'host': 'nxos1.lasthop.io',
 'username': 'pyclass',
 'password': '88newclass'
},
{
 'device_type': 'cisco_nxos',
 'host': 'nxos2.lasthop.io',
 'username': 'pyclass',
 'password': '88newclass'
}

]

for device in list_nxos:
  net_connect = ConnectHandler(**device)
  print(net_connect.find_prompt())
