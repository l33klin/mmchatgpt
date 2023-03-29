#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    : model
@Purpose : 
@Author  : jian.li
@Contact : jian.li@shopee.com
@Time    : 2023/3/29 5:39 PM
@Refs    :
"""
from collections import namedtuple

RedisCfg = namedtuple("RedisCfg", ("host", "username", "password", "port", "db"))
