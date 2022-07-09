import yaml
from pathlib import Path
from netmiko import ConnectHandler


filename = Path("~/.netmiko.yml")

with open(filename.expanduser()) as f:
    # pyyaml made a backwards incompatible change to .load()
    # the simple fix is just to call .safe_load() instead
    yaml_out = yaml.safe_load(f)

cisco3 = yaml_out["cisco3"]
net_connect = ConnectHandler(**cisco3)

print()
print(net_connect.find_prompt())
print()
