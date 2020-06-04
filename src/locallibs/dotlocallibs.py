import os
import re
from collections import OrderedDict


class DotLocalLibs:
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
        for line in _lines:
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
        self._options.update(options)

        libpaths = []
        for path in lines:
            if os.path.isabs(path):
                abspath = path
            else:
                abspath = os.path.abspath(path)
            libpaths.append(abspath)

        self._lib_base_paths.extend(libpaths)
