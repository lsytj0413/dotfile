#coding=utf-8
'''
目录访问模块
pip install enum
'''

import os
from functools import wraps

from enum import Enum


class WalkType(Enum):
    '''访问文件类型定义'''
    FILE = 0
    DIRECTORY = 1
    ALL = 2


def walk(wtype=WalkType.ALL):
    '''
    遍历目录

    args:
        wtype: 遍历类型, WalkType
    '''
    assert isinstance(wtype, (WalkType))

    def walk_imp(fn):
        '''
        处理函数

        args:
            fn: 包裹函数
        '''
        @wraps(fn)
        def walk_wrapper(dir_path):
            '''
            遍历目录

            args:
                dir_path: 目录路径
            '''
            for file_name in os.listdir(dir_path):
                file_path = os.path.join(dir_path, file_name)
                if  wtype == WalkType.ALL:
                    fn(file_path)
                elif wtype == WalkType.FILE and \
                     os.path.isfile(file_path):
                    fn(file_path)
                elif wtype == WalkType.DIRECTORY and \
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
