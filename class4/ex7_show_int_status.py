#!/usr/bin/env python

import textfsm
from pathlib import Path
from pprint import pprint

p = Path('eth2_1_output.txt').read_text()
#eth2_1_output = p.read_text()

with open('eth2_1.tpl') as template:
  fsm = textfsm.TextFSM(template)
  result = fsm.ParseText(p)

print(fsm.header)
print(result)



results = list()
for item in result:
    results.append(dict(zip(fsm.header, item)))
pprint(results)
