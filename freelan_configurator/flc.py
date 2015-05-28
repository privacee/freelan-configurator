#!/usr/bin/env python

from __future__ import print_function
try:
   input = raw_input
except NameError:
   pass


import os,sys
import subprocess

VERBOSE = False

def run_with_permissions_osx(apple_script, args=[]):

    return os.system("osascript -e '" + apple_script + "'")

    #p = subprocess.Popen(['osascript', '-'] + args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #stdout, stderr = p.communicate(apple_script)
    #p.wait()
    #print(stdout)
    #return stdout

def run_without_permissions():
    cmd = """
          do shell script "./freelan_cmd.py -l"
          """
    return run_with_permissions_osx(cmd)

def run_with_permissions():
    cmd = """
          do shell script "./freelan_cmd.py -l -server -w" with administrator privileges
          """
    return run_with_permissions_osx(cmd)

def help():
    print("freelan configurator")

def main(argv):
    global VERBOSE

    VERBOSE = False

    print("We will ask for elevated admin permissions by default to write the config file.")
    print("Do you instead prefer to run with user rights? (y,n)")
    y_n = input()

    if y_n.startswith('y'):
        print("This may result in file permission error when writing config files to system directories.")
        return run_without_permissions()

    return run_with_permissions()


if __name__ == "__main__":
    main(sys.argv[1:])