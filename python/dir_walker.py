#coding=utf-8

import os
import sys

def dir_walker(walk_obj, dir_path):
    for file_name in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file_name)
        if os.path.isfile(file_path):
            walk_obj.on_file(dir_path, file_name)
        elif os.path.isdir(file_path):
            walk_obj.on_dir(dir_path, file_name)
            if walk_obj.is_recursion(file_path):
                dir_walker(walk_obj, file_path)
