import os


def get_abs_path(base_dir):
    """
    Simply checks if a dir is absolute or not and then return the absolute path.
    :param base_dir:
    :return:
    """
    abs_base_dir = base_dir
    if not os.path.isabs(abs_base_dir):
        abs_base_dir = os.path.abspath(abs_base_dir)
    return abs_base_dir

