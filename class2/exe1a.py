#!/usr/bin/env/ python
from netmiko import ConnectHandler

device1 = {
'device_type': 'cisco_ios',
'host': 'cisco3.lasthop.io',
'username': 'pyclass',
'password': '88newclass',
}

con = ConnectHandler (**device1)

output = con.send_command_timing('ping', strip_command=False,strip_prompt=False)
output += con.send_command_timing('\n', strip_command=False,strip_prompt=False)
output += con.send_command_timing('8.8.8.8', strip_command=False,strip_prompt=False)
output += con.send_command_timing('\n', strip_command=False,strip_prompt=False)
output += con.send_command_timing('\n', strip_command=False,strip_prompt=False)
output += con.send_command_timing('\n', strip_command=False,strip_prompt=False)
output += con.send_command_timing('\n', strip_command=False,strip_prompt=False)
output += con.send_command_timing('\n', strip_command=False,strip_prompt=False)

print(output)
