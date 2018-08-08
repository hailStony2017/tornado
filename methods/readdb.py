#!/usr/bin/env Python
# coding=utf-8

# from .db import *


def select_table(table, column, condition, value):
    # sql = "select {} from {} where {} = '{}'".format(column, table, condition, value)
    # cur.execute(sql)
    # lines = cur.fetchall()
    lines = ((1, 'qq', '123123', 'qq@gmail.com'),)
    return lines


def select_columns(table, column):
    # sql = "select {} from {}".format(column, table)
    # cur.execute(sql)
    # lines = cur.fetchall()
    lines = ((1, 'qq', '123123', 'qq@gmail.com'),)
    return lines
