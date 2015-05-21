#!/usr/bin/env python

from __future__ import print_function

import sys
import freelan_cmd as FreelanCMD
from freelan_cfg import FreelanCFG

VERBOSE = False

def help():
    print("freelan configurator")

def main(argv):
    global VERBOSE

    VERBOSE = False

    fcfg = FreelanCMD.load_config()

    FreelanCMD.write_config(fcfg)


if __name__ == "__main__":
    main(sys.argv[1:])