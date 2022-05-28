#! /usr/bin/env python

from netmiko import ConnectHandler

nxos = {
 'device_type': 'cisco_nxos',
 'host': 'nxos1.lasthop.io',
 'username': 'pyclass',
 'password': '88newclass'
}

net_connect = ConnectHandler(**nxos)

print(net_connect.find_prompt())
