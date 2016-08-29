#coding=utf-8

from enum import Enum


class WalkType(Enum):
    FILE = 0
    DIRECTORY = 1
    ALL = 2


def walk(type):
    '''
    遍历目录

    args:
        type: 遍历类型, WalkType
    '''
    assert isinstance(type, (WalkType))

    def walk_imp(fn):
        '''
        处理函数

        args:
            fn: 包裹函数
        '''
        def walk_wrapper(dir_path):
            '''
            遍历目录

            args:
                dir_path: 目录路径
            '''
            import os
            import sys
            for file_name in os.listdir(dir_path):
                file_path = os.path.join(dir_path, file_name)
                if  type == WalkType.ALL:
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
    # @walk(WalkType.FILE)
    # def printer(file_name):
    #     print file_name
    #     import os
    #     if os.path.isdir(file_name):
    #         print "Dir"
    #         printer(file_name)

    # printer("/home/lsytj/dotfile")
    print 'DirWalker module'
