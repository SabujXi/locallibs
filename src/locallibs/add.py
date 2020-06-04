import os
import sys

from locallibs.dotlocallibs import DotLocalLibs


def add_locallibs(base_dir):
    if not os.path.isabs(base_dir):
        base_dir = os.path.abspath(base_dir)

    config_file_path = os.path.join(base_dir, '.locallibs')
    if not os.path.exists(config_file_path):
        # bail
        return None
    # do the math
    dotlocallibs = DotLocalLibs(config_file_path)
    lib_base_paths = list(dotlocallibs.get_base_paths())
    lib_base_paths.reverse()
    sys.path.insert(os.path.join(base_dir, '_locallibs'))
    for include_path in lib_base_paths:
        sys.path.insert(0, include_path)

    return lib_base_paths