#!/usr/bin/env python
from pprint import pprint

arp = """
Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
"""
my_list = []
my_dict = {}
new_arp = arp.splitlines()
i = 2
while i < 7:
  _,ip_addr,_,mac_addr,_,intf = new_arp[i].split()
  my_dict = {'ip_addr':ip_addr, 'mac_addr':mac_addr,'intf':intf}
  my_list.append(my_dict)
  i += 1

pprint(my_list)
