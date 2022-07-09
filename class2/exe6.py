#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
import time

password = getpass()

cisco4 ={
 'device_type': 'cisco_ios',
 'host': 'cisco4.lasthop.io',
 'username': 'pyclass',
 'password': password,
 'secret': password,
 'session_log': 'my_output.txt'
}

con = ConnectHandler(**cisco4)
con.find_prompt()
con.config_mode()
con.exit_config_mode()
con.find_prompt()
con.write_channel('disable\n')
time.sleep(2)
con.read_channel()
con.enable()    
con.find_prompt()
        
