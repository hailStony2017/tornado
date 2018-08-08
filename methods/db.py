#!/usr/bin/env Python
# coding=utf-8

import pymysql

# Connection object
conn = pymysql.connect(host='localhost',user='root',password='25264744', db='yqtest', port=3306, charset='utf8')

# Cursor object
cur = conn.cursor()