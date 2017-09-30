#!/grid/common/pkgs/python/v3.6.0/bin/python3.6
with open("device", "r") as f:
    for line in f:
        data = line.strip()
        if data: # is not empty
          raw_data2 = data
          if not raw_data2.startswith(('Total', 'MAC')):
            getMac = raw_data2[:15]
            print(getMac.upper())
