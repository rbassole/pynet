Value Filldown ROUTER_ID (\S+)
Value Filldown LOCAL_AS (\S+)
Value NEIGHBOR (\S+)
Value REMOTE_AS (\d+)
Value UP_DOWN (\S+)
Value PREFIX (\S+)

Start
  ^BGP router identifier ${ROUTER_ID}, local AS number ${LOCAL_AS}$$
  ^Neighbor.*State/PfxRcd.*$$ -> ShowBGP

ShowBGP
  ^${NEIGHBOR}\s+\d+\s+${REMOTE_AS}\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+${UP_DOWN}\s+${PREFIX} -> Record

EOF
