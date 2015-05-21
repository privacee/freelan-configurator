#!/usr/bin/env python

from __future__ import print_function

import os, sys
import appdirs

from freelan_cfg import FreelanCFG

def load_config():
    '''try loading config file from a default directory'''
    cfg_path = '/usr/local/etc/freelan'
    cfg_file = 'freelan.cfg'

    if not os.path.isdir(cfg_path):
        print("Can not find default freelan config directory.")
        return

    cfg_file_path = os.path.join(cfg_path,cfg_file)

    if not os.path.isfile( cfg_file_path ):
        print("Can not find default freelan config file.")
        return

    return _load_config(cfg_file_path)

def _load_config(cfg_file_path):

    if not os.path.isfile( cfg_file_path ):
        print("Can not find freelan config file at: " + cfg_file_path)
        return

    cfg_lines = []
    with open(cfg_file_path, 'r') as cfg:
        # remove leading whitespaces and tailing characters
        cfg_lines = [cfg_line.strip() for cfg_line in cfg]
        # remove comments and empty lines (not the most efficient way, yes ...)
        cfg_lines = [cfg_line for cfg_line in cfg_lines if not cfg_line.startswith('#') and len(cfg_line) > 0]

    fcfg = FreelanCFG()

    return fcfg

def help():
    print("freelan configurator")

def main(argv):
    cfg = load_config()
    cfg.print()


if __name__ == "__main__":
    main(sys.argv[1:])