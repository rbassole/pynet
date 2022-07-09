#!/usr/bin/env python

from netmiko import ConnectHandler

nxos =[{
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
}]

for device in nxos:
    with ConnectHandler(**device) as con:
        output = con.send_config_from_file('vlan.txt')
        output += con.save_config()
        print(output)
    
        
