#!/usr/bin/env/ python
from netmiko import ConnectHandler

device1 = {
'device_type': 'cisco_ios',
'host': 'cisco3.lasthop.io',
'username': 'pyclass',
'password': '88newclass',
}

con = ConnectHandler (**device1)
output = con.send_command('ping', expect_string=r'Protocol',strip_command=False,strip_prompt=False)
output += con.send_command('\n', expect_string=r'Target',strip_command=False,strip_prompt=False)
output += con.send_command('8.8.8.8', expect_string=r'Repeat',strip_command=False,strip_prompt=False)
output += con.send_command('\n', expect_string=r'Datagram',strip_command=False,strip_prompt=False)
output += con.send_command('\n', expect_string=r'Timeout',strip_command=False,strip_prompt=False)
output += con.send_command('\n', expect_string=r'Extended',strip_command=False,strip_prompt=False)
output += con.send_command('\n', expect_string=r'Sweep',strip_command=False,strip_prompt=False)
output += con.send_command_timing('\n', strip_command=False,strip_prompt=False)

print(output)
