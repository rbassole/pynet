import pyeapi
from getpass import getpass
from pprint import pprint as pp
from my_funcs import function1, function2

def main():
  device_dict = function1('device.yml')

  for key,devices in device_dict.items():
    devices['password'] = getpass() 
    connection = pyeapi.client.connect(**devices)
    node = pyeapi.client.Node(connection)
    output = node.enable('show ip arp')
    a_list = output[0]['result']['ipV4Neighbors']
    function2(a_list)

if __name__ == "__main__":
  main()
