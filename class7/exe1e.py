from lxml import etree

with open('show_security_zones.xml', 'r') as f:
  content = f.read().strip()
  my_xml = etree.fromstring(content)
  trust_zone = my_xml[0][0].text
  print(trust_zone)
 
