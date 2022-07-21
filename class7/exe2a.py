import xmltodict
from pprint import pprint as pp

with open('show_security_zones.xml','r') as f:
  content = f.read()
  my_xml = xmltodict.parse(content)
  print('Print the new variable and its type:')
  print()
  pp(my_xml)
  print(type(my_xml))
