# Platform
Windows x64

# Requirements
Python 3.7
Django
MySQL Server
mysqlclient

# Installation

## MySQL Server

See: https://dev.mysql.com/downloads/mysql/
We'll be using username root password root and legacy authentication (mysql_native_password) for development purposes. See: https://stackoverflow.com/questions/49931541/mysql-changing-authentication-type-from-standard-to-caching-sha2-password

## Python

See: https://www.python.org/downloads/
Adding Python to your PATH system variable is recommended. See: https://geek-university.com/python/add-python-to-the-windows-path/

Additionally, working under a virtual environment is preferred.
Create a virtual environment in the root folder of this repository:

> virtualenv .

To activate the virtual environment:

> .\scripts\activate

## Django

See: https://docs.djangoproject.com/en/2.1/topics/install/

Install Django using pip.

> pip install django

## mysqlclient

Currently, the mysql-connector for Python 3.7 is not available in the official website. See: https://stackoverflow.com/questions/51117503/python-3-7-failed-building-wheel-for-mysql-python

E.g.: grab a copy of mysqlclient‑1.4.1‑cp37‑cp37m‑win_amd64.whl from https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient and install it using pip.

> pip install path/to/mysqlclient‑1.4.1‑cp37‑cp37m‑win_amd64.whl
