# Platform
* Windows x64

# Requirements
* Python 3.7
* Django
* MySQL Server
* mysqlclient

# Installation

## MySQL Server

See: https://dev.mysql.com/downloads/mysql/

Important: for testing purposing we'll be using **username root password root**, as well as **legacy authentication (mysql_native_password)** for development purposes. See: https://stackoverflow.com/questions/49931541/mysql-changing-authentication-type-from-standard-to-caching-sha2-password

Use the following statement to **create the database db_unapec_caja**.

> CREATE DATABASE `db_unapec_caja` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;

## Python

See: https://www.python.org/downloads/

Adding Python to your PATH system variable is recommended. Commands below will assume you've done so. See: https://geek-university.com/python/add-python-to-the-windows-path/

Additionally, working under a virtual environment is preferred. Create a virtual environment in the **root folder** of this repository with:

> virtualenv .

To activate the virtual environment, in the **root folder** do:

> .\scripts\activate

## Django

See: https://docs.djangoproject.com/en/2.1/topics/install/

Install Django using pip.

> pip install django

## mysqlclient

Currently, the mysql-connector for Python 3.7 is not available in the official website. See: https://stackoverflow.com/questions/51117503/python-3-7-failed-building-wheel-for-mysql-python

Grab a copy from https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient and install it using pip.

> pip install path/to/mysqlclient‑1.4.1‑cp37‑cp37m‑win_amd64.whl

# Run

While in the rool folder, do:

> cd django

> manage.py runserver

## Code First

To prepare changes for the database:

> manage.py makemigrations

To apply changes to the database:

> manage.py migrate
