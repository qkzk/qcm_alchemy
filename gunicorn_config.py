"""
title: gunicorn configuration file
author: qkzk
date: 2021/06/28
"""

chdir = "app"
loglevel = "info"
workers = 3
bind = "0.0.0.0:8989"
