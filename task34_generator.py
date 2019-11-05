ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
routes = ((start, stop) for start in ports for stop in ports[ports.index(start)])

i = 0
for route in routes:
    print(routes)
    i += 1

print(i)
