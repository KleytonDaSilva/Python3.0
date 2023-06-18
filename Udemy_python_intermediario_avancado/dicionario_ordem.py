# criar um diionarios e mandar a ordem
from collections import OrderedDict

d = OrderedDict()
d['Python'] = 10
d['Java'] = 5
d['Php'] = 6
d['C'] = 10
for key in d:
    print(key, d[key])

d2 = {}
d2['Python'] = 10
d2['Java'] = 5
d2['Php'] = 6
d2['C'] = 10
for key in d2:
    print(key, d2[key])