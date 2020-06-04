import os
import shutil

from locallibs.dotlocallibs import DotLocalLibs


def collect_locallibs(base_dir):
    if not os.path.isabs(base_dir):
        base_dir = os.path.abspath(base_dir)

    config_file_path = os.path.join(base_dir, '.locallibs')
    if not os.path.exists(config_file_path):
        # bail
        return None
    # do the math
    dotlocallibs = DotLocalLibs(config_file_path)
    lib_base_paths = list(dotlocallibs.get_base_paths())

    collect_dir = os.path.join(base_dir, '_locallibs')
    if not os.path.exists(collect_dir):
        os.makedirs(collect_dir)

    # clean _locallibs
    _path_names = os.listdir(collect_dir)
    for _path_name in _path_names:
        _full_path = os.path.join(collect_dir, _path_name)
        if os.path.isfile(_full_path):
            os.remove(_full_path)
        else:
            shutil.rmtree(_full_path)

    for lib_base_path in lib_base_paths:
        _path_names = os.listdir(lib_base_path)
        for _path_name in _path_names:
            _full_path = os.path.join(lib_base_path, _path_name)
            if os.path.isfile(_full_path):
                shutil.copy(_full_path, collect_dir)
            else:
                shutil.copytree(_full_path, os.path.join(collect_dir, _path_name))

    return lib_base_paths
