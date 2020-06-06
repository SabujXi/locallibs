import os
import sys

from locallibs.collect import collect_locallibs


def locallibs_cli():
    args = sys.argv[1:]
    if len(args) == 0:
        print("No command provided. Supported commands: collect")
    if args[0] == 'collect':
        res = collect_locallibs(os.getcwd())
        if res is None:
            print("Config file <.locallibs> does not exist")
        else:
            if len(res) == 0:
                print("No path found in config and not copying anything.")
            for path in res:
                print("Copied: " + path)
    else:
        print("Invalid command. Supported commands: collect")