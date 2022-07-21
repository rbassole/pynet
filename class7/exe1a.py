from lxml import etree

with open('show_security_zones.xml', 'r') as f:
  content = f.read().strip()
  my_xml = etree.fromstring(content)
  print(my_xml)
  print(type(my_xml))
