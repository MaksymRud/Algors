#sum(c.values())                 # total of all counts 
#c.clear()                       # reset all counts 
#list(c)                         # list unique elements 
#set(c)                          # convert to a set 
#dict(c)                         # convert to a regular dictionary c.items()  
#c.items()                       # convert to a list like (elem, cnt) 
#Counter(dict(list_of_pairs))    # convert from a list of(elem, cnt) 
#c.most_common()[:-n-1:-1]       # n least common elements 
#c += Counter()                  # remove zero and negative counts
"""
c = Counter('abcacdabcacd')
print(c)
Counter({'a': 4, 'c': 4, 'b': 2, 'd': 2})

"""