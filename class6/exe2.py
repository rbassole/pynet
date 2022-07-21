import pyeapi
import os
import yaml
from getpass import getpass
import ipdb

def yaml_load_devices(filename):
  with open(filename,'r') as f:
    return yaml.safe_load(f)
  raise ValueError('Reading YAML file failed')

def main():
  devices = yaml_load_devices('device.yml')
  password = os.getenv('PYNET_PASSWORD') if os.getenv('PYNET_PASSWORD') else getpass()

  for name,device_dict in devices.items():
    device_dict['password'] = password
    connection = pyeapi.client.connect(**device_dict)
    node = pyeapi.client.Node(connection)
    output = node.enable('show ip arp')

    print()
    print('_' * 40)
    arp_list = output[0]['result']['ipV4Neighbors']
    for arp_entry in arp_list:
      mac_address = arp_entry['hwAddress']
      ip_address = arp_entry['address']
      print('{:^15}{:^5}{:^15}'.format(ip_address, "-->", mac_address))
    print('_' * 40)
    print()

if __name__ == "__main__":
  main() 
