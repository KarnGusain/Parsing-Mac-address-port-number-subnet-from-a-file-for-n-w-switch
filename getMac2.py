#!/grid/common/pkgs/python/v3.6.0/bin/python3.6
import re
for line in open('device'):
  line = line.strip()
  if line != '':
    if not re.match(r'(Total|MAC)', line):
      getMac = line[:15]
      getPort = line[15:20]
      getSub = line[36:40]
      #getMAC = line[15:20]
      print(getMac.upper())
      #print(getPort.upper())
      #print(getSub.upper())

