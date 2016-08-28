#coding=utf-8

from enum import Enum


class WalkType(Enum):
    FILE = 0
    DIRECTORY = 1
    ALL = 2


def walk(type):
    def walk_imp(fn):
        def walk_wrapper(dir_path):
            import os
            import sys
            for file_name in os.listdir(dir_path):
                file_path = os.path.join(dir_path, file_name)
                if type == WalkType.ALL:
                    fn(file_path)
                elif type == WalkType.FILE and \
                     os.path.isfile(file_path):
                    fn(file_path)
                elif type == WalkType.DIRECTORY and \
                     os.path.isdir(file_path):
                    fn(file_path)
        return walk_wrapper
    return walk_imp


if __name__ == '__main__':
    print 'DirWalker module'
