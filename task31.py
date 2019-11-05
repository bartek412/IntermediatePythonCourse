ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
conections_p2p = [(p, q) for p in ports for q in ports if p > q]
print(conections_p2p)
print(len(conections_p2p))