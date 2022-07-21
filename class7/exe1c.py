from lxml import etree

with open('show_security_zones.xml', 'r') as f:
  content = f.read().strip()
  my_xml = etree.fromstring(content)
  print(my_xml.tag)
  print(len(my_xml.getchildren()))
