__all__ = [
    'add_locallibs',
    'collect_locallibs',
    'locallibs_cli'
]

import sys
import os
import re
from collections import OrderedDict
import shutil


def add_locallibs(base_dir):
    if not os.path.isabs(base_dir):
        base_dir = os.path.abspath(base_dir)

    config_file_path = os.path.join(base_dir, '.locallibs')
    if not os.path.exists(config_file_path):
        # bail
        return
    # do the math
    dotlocallibs = _DotLocalLibs(config_file_path)
    lib_base_paths = list(dotlocallibs.get_base_paths())
    lib_base_paths.reverse()
    for include_path in lib_base_paths:
        sys.path.insert(0, include_path)


def collect_locallibs(base_dir):
    if not os.path.isabs(base_dir):
        base_dir = os.path.abspath(base_dir)

    config_file_path = os.path.join(base_dir, '.locallibs')
    if not os.path.exists(config_file_path):
        # bail
        return
    # do the math
    dotlocallibs = _DotLocalLibs(config_file_path)
    lib_base_paths = list(dotlocallibs.get_base_paths())

    collect_dir = os.path.join(base_dir, '_locallibs')
    if not os.path.exists(collect_dir):
        os.makedirs(collect_dir)

    # cleal _locallibs
    _paths = os.listdir(collect_dir)
    for _path in _paths:
        _full_path = os.path.join(collect_dir, _path)
        if os.path.isfile(_full_path):
            os.remove(_full_path)
        else:
            shutil.rmtree(_full_path)

    for lib_base_path in lib_base_paths:
        print("Copying: " + lib_base_path)
        shutil.copytree(lib_base_path, collect_dir)


def locallibs_cli():
    args = sys.argv[1:]
    if not args:
        print("No command provided. Supported commands: collect")
    if args[0] == 'collect':
        collect_locallibs(os.getcwd())
    else:
        print("Invalid command. Supported commands: collect")


class _DotLocalLibs:
    _option_pat = re.compile(r":(?P<key>[a-z0-9_-]+)\s*=\s*(P?<value>.*)", re.IGNORECASE)

    def __init__(self, file_name: str):
        self._file_name = file_name
        self._options = OrderedDict()
        self._lib_base_paths = []
        # parse
        self.__parse(self._file_name)

    def get_option(self, name):
        return self._options[name]

    def get_base_paths(self):
        return tuple(self._lib_base_paths)

    def __parse(self, file_name: str):
        with open(file_name, encoding='utf-8') as f:
            _lines = f.readlines()

        lines = []
        for line in lines:
            line = line.strip()
            if line == '' or line.startswith('#'):
                continue
            lines.append(line)

        # extract options
        options = OrderedDict()
        while lines:
            line = lines[0]
            opt_match = self._option_pat.match(line)
            if not opt_match:
                break

            key = opt_match.group('key')
            value = opt_match.group('value')
            options[key] = value
            lines.pop(0)

        libpaths = []
        for path in lines:
            if os.path.isabs(path):
                abspath = path
            else:
                abspath = os.path.abspath(path)
            libpaths.append(abspath)

        self._options = options
        self._lib_base_paths = libpaths
