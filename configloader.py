#!/usr/bin/python
# -*- coding: utf-8 -*-
import importloader

g_config = None


def load_config():
    global g_config
    g_config = importloader.loads(['userapiconfig', 'apiconfig'])


def get_config():
    return g_config

load_config()
