# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import py.path
import subprocess
from os import path as osp


BASE_DIR = osp.dirname(osp.dirname(osp.abspath(__file__)))


def path(*name):
    return py.path.local(BASE_DIR).join(*name)


def strpath(*name):
    return path(*name).strpath


def info(*msg, **kwargs):
    print(*msg, **kwargs)


def run(cmd, **kwargs):
    cmdline = subprocess.list2cmdline(cmd)
    info('{}:\n  {}'.format(os.getcwd(), cmdline))
    subprocess.check_call(cmd, **kwargs)
