#Value INTERFACE (Ethernet.\/.)
Value INTERFACE (\S+)
Value LINE (up|down)
Value STATE (\w+)
Value MTU (\d+)
Value MAC_ADD (\S+)
Value DUPLEX (\w+)
Value SPEED (\d+)

Start
 ^${INTERFACE} is ${LINE}$$ 
 ^admin state is ${STATE}
 ^  Hardware:  Ethernet, address: ${MAC_ADD} .*$$
 ^  MTU ${MTU} bytes.*usec$$
 ^  ${DUPLEX}-duplex, ${SPEED} Mb/s$$ -> Record

EOF
