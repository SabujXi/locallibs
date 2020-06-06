import os
import sys
from .path import get_abs_path

from locallibs.dotlocallibs import DotLocalLibs


def add_locallibs_from_config(base_dir):
    """
    Responsible for including the library directories (directories containing the local library) found in the config
     files `.locallibs` to the the
     the system path, that is `sys.path`.
    It will prepend the directories instead of appending, so that they gets precedence.  
    :param base_dir: the directory where the .locallibs config file exists.
    :return: the list of library roots prepended to the system path.
    """
    abs_base_dir = get_abs_path(base_dir)

    config_file_path = os.path.join(abs_base_dir, '.locallibs')
    if not os.path.exists(config_file_path):
        # bail
        return None
    # do the math
    dotlocallibs = DotLocalLibs(config_file_path)
    lib_base_paths = list(dotlocallibs.get_base_paths())
    lib_base_paths.reverse()
    for include_path in lib_base_paths:
        sys.path.insert(0, include_path)

    # Add collected locallibs to the system path - appened due to the lowest precedence.
    sys.path.append(os.path.join(abs_base_dir, '_locallibs'))  # collected locallibs exist in cwd/_locallibs

    return lib_base_paths
