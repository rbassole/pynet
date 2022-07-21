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
    output = node.enable('show ip route')
    r_list = output[0]['result']['vrfs']['default']['routes']
    print()
    for route,route_dict in r_list.items():
      if route_dict['routeType'] == 'static':
        print(f"{route} --> {route_dict['vias'][0]['nexthopAddr']}")
      else:
        print(f"{route} --> {route_dict['vias'][0]['interface']}")

if __name__ == "__main__":
  main()
