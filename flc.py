#!/usr/bin/env python

from __future__ import print_function

import os, sys
#import appdirs

from freelan_cfg import FreelanCFG

VERBOSE = False

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
    global VERBOSE

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
    fcfg_section = None

    for cfg_line in cfg_lines:
        if VERBOSE:
            print("Loading: " + cfg_line)
        if cfg_line.startswith('[') and cfg_line.endswith(']'):
            section_name = cfg_line[1:-1]
            fcfg_section = getattr(fcfg, section_name)
            continue

        if '=' in cfg_line:
            kv_list = cfg_line.split('=')
            if not len(kv_list) is 2:
                print("Issue with config line: " + cfg_line)
                continue

            cur_v = getattr(fcfg_section, kv_list[0])
            def_v = fcfg_section.defaults[kv_list[0]]

            # if cur_v None simply overwrite it!
            if cur_v is None:
                setattr(fcfg_section, kv_list[0], kv_list[1])
                continue

            # if cur_v is a string or bool, make it a list and expand it with new value
            if isinstance(cur_v, basestring) or isinstance(cur_v, bool):
                cur_v = [cur_v]

            cur_v.append(kv_list[1])
            setattr(fcfg_section, kv_list[0], cur_v)



    return fcfg


def write_config(overwrite=False):
    '''try writing config file to a default directory'''
    cfg_path = '/usr/local/etc/freelan'
    cfg_file = 'freelan.cfg'

    if not os.path.isdir(cfg_path):
        print("Can not find default freelan config directory.")
        return

    cfg_file_path = os.path.join(cfg_path,cfg_file)

    if os.path.isfile( cfg_file_path ) and not overwrite:
        print("freelan config file already exists - please use --overwrite flag to replace it.")
        return

def help():
    print("freelan configurator")

def main(argv):
    global VERBOSE

    VERBOSE = False

    cfg = load_config()
    cfg.print()


if __name__ == "__main__":
    main(sys.argv[1:])