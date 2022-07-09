Value MAC_ADD (\S+)
Value IP_ADD (([0-9]{1,3}\.){3}[0-9]{1,3})
Value NAME (([0-9]{1,3}\.){3}[0-9]{1,3})
Value INTERFACE (\S+)

Start
  ^MAC Address.*Flags$$ -> ShowARP

ShowARP
 ^${MAC_ADD}\s+${IP_ADD}\s+${NAME}\s+${INTERFACE} -> Record

EOF
