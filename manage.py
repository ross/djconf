#!/usr/bin/env python

from __future__ import absolute_import

from django.core.management import execute_from_command_line
from os import environ
from sys import argv

if len(argv) > 1 and argv[1] == 'test':
    environ['ENV'] = 'test'

if __name__ == '__main__':
    environ.setdefault('DJANGO_SETTINGS_MODULE', 'www.settings')

    execute_from_command_line(argv)
