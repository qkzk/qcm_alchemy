"""
title: main
author: qkzk
date: 2021/05/10

Creates an app and run it.
Used to run the app with flask in debug mode AKA developpment
"""
from src import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0")
