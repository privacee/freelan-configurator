#!/usr/bin/env python

from __future__ import print_function

import sys
import subprocess

VERBOSE = False

def help():
    print("freelan configurator")

def main(argv):
    global VERBOSE

    VERBOSE = False


if __name__ == "__main__":
    main(sys.argv[1:])