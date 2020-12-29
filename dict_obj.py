from collections import defaultdict 

class Node:
    def __init__(self, attr):
        self._attr = attr
    
    @property
    def attr(self):
        return self._attr

    @attr.setter
    def attr(self, val):
        self._attr = val

d = defaultdict(list)
n = Node(5)
d[5].append(n)

d[3].append(n)

v = Node(111)
d[n].append(v)
del d[5], d[3]

n.attr = 3
    
for u in d.keys():
    print(u.attr)

 
print(d)
