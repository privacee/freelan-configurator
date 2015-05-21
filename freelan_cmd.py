#!/usr/bin/env python

from __future__ import print_function

import os, sys
import shutil
import time
import datetime

#import appdirs

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
    with open(cfg_file_path, 'r') as cfg_f:
        # remove leading whitespaces and tailing characters
        cfg_lines = [cfg_line.strip() for cfg_line in cfg_f]
        # remove comments and empty lines (not the most efficient way, yes ...)
        cfg_lines = [cfg_line for cfg_line in cfg_lines if not cfg_line.startswith('#') and len(cfg_line) > 0]

    fcfg = FreelanCFG()
    fcfg_section = None

    for cfg_line in cfg_lines:
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


def write_config(cfg):
    '''try writing config file to a default directory'''
    cfg_path = '/usr/local/etc/freelan'
    cfg_file = 'freelan_TEST.cfg'

    cfg_lines = []

    if not isinstance(cfg, FreelanCFG):
        if not isinstance(cfg, (list, tuple)):
            print("Freelan write input can not be processed.")
            return
        cfg_lines = cfg
    else:
        cfg_lines = cfg.build()

    if not os.path.isdir(cfg_path):
        print("Can not find default freelan config directory.")
        return

    cfg_file_path = os.path.join(cfg_path,cfg_file)

    if os.path.isfile( cfg_file_path ):
        print("freelan config file already exists - moving to not replace content.")
        ts = time.time()
        backup_file = cfg_file_path+'.ORG-'+datetime.datetime.fromtimestamp(ts).strftime('%y-%m-%d-%H-%M-%S')
        shutil.move(cfg_file_path, backup_file)

    with open(cfg_file_path, 'w') as cfg_f:
        cfg_f.writelines(cfg_lines)

def generate_server_cfg():
    fcfg = FreelanCFG()
    return fcfg

def generate_client_cfg():
    fcfg = FreelanCFG()
    return fcfg

def generate_cfg():
    fcfg = FreelanCFG()
    return fcfg

def main(argv):

    fcfg = FreelanCFG()

    if '-l' in argv:
        fcfg = load_config()

    if '-server' in argv:
        fcfg = generate_server_cfg()

    if '-client' in argv:
        fcfg = generate_client_cfg()

    if '-generate' in argv:
        fcfg = generate_cfg()

    if '-p' in argv:
        fcfg.print()

    if '-w' in argv:
        write_config(fcfg)


if __name__ == "__main__":
    main(sys.argv[1:])