#!/usr/bin/python3
"""
title: gunicorn configuration file
author: qkzk
date: 2022/09/12
"""
from src import on_starting as src_on_starting

print("on_starting")

chdir = "app"
loglevel = "info"
workers = 3
bind = "0.0.0.0:443"
on_starting = src_on_starting
