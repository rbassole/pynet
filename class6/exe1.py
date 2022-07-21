import pyeapi
from pprint import pprint as pp

node = pyeapi.connect_to('arista3')
output = node.enable('show ip arp')

my_list = output[0]['result']['ipV4Neighbors']

for item in my_list:
  print(f"{item['hwAddress']} --> {item['address']}")
  
  

