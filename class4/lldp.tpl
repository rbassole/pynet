Value DEVICE (\S+)
Value LOCAL_INTF (\S+)
Value CAPABILITY (\S+)
Value PORT (\S+)

Start
  ^Device ID.*Port ID -> ShowLLDP

ShowLLDP
  ^${DEVICE}\s+${LOCAL_INTF}\s+\d+\s+${CAPABILITY}\s+${PORT} -> Record

EOF
