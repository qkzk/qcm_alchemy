import collections

try:
    from collections import abc

    collections.MutableMapping = abc.MutableMapping
except:
    pass
