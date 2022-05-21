"""
title: fix collections import
author: qkzk
date: 2022/05/10

Fix the wrong import of collections

collections.MutableMapping was previously called abc.MutableMapping
and have to be renamed to be compatible with new packages using the
new paths.
"""
import collections

try:
    from collections import abc

    collections.MutableMapping = abc.MutableMapping
except:
    pass
