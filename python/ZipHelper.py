#coding=utf-8
'''zip 帮助类模块'''

import os
import zipfile


class ZipException(Exception):
    '''Exception'''
    pass


def zip_folder(dir_path, zip_filename):
    '''
    压缩文件夹.
    args:
        dir_path: 需要压缩的目录
        zip_file_name: 压缩文件的名称
    return:
        bool
    exceptions:
        ZipException
    '''
    try:
        dir_path = os.path.realpath(dir_path).replace('\\', '/')
        zip_file = zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED)
    except Exception as ex:
        raise ZipException("can't open file '{}'".format(ex))
    try:
        # 提取当前目录
        zip_dirs = [os.path.split(dir_path)[1]]
        __zip_folder(zip_file, zip_dirs, dir_path)
        return True
    except Exception as ex:
        raise ZipException("zip process error {}".format(ex))
    finally:
        zip_file.close()


def __zip_folder(zip_file, zip_dirs, current_dir):
    '''
    压缩文件夹, 深度优先
    args:
        zip_file: 压缩文件对象
        zip_dirs: 待压缩的目录
        current_dir: 当前目录
    '''
    #添加文件夹项
    zip_file.writestr('/'.join(zip_dirs) + '/', '')
     #遍历文件夹
    for filename in os.listdir(current_dir):
        full_file_name = os.path.join(current_dir, filename)
        if os.path.isdir(full_file_name):
            #遍历到文件夹，递归zip
            zip_dirs.append(filename)
            __zip_folder(zip_file, zip_dirs, full_file_name)
        else:
            #遍历到文件，压入zip
            zip_name = '/'.join(zip_dirs) + '/' + filename
            zip_file.write(full_file_name, zip_name)
        zip_dirs.pop()

def unzip_to_folder(dir_path, unzip_file_name):
    '''
    解压缩到文件夹。
    args:
        dir_path: 需要压缩的目录
        zip_file_name: 压缩文件的名称
    return:
        bool
    exceptions:
        ZipException
    '''
    try:
        zip_file = zipfile.ZipFile(unzip_file_name, 'r')
    except Exception, ex:
        raise ZipException("can't open file '{}'".format(ex))
    try:
        for zip_name in zip_file.namelist():
            zip_name = zip_name.replace('\\', '/')
            if zip_name.endswith('/'):
                #目录项
                __unzip_folder_item(zip_file, zip_name, dir_path)
            else:
                #文件项
                __unzip_file_item(zip_file, zip_name, dir_path)
        return True
    except Exception, ex:
        raise ZipException("unzip process error {}".format(ex))
    finally:
        zip_file.close()


def __unzip_folder_item(zip_file, item_name, dir_path):
    '''
    解压文件夹项
    args:
        zip_file: 压缩文件对象
        item_name: 压缩项名称
        dir_path: 解压目录
    '''
    dir_path = os.path.join(dir_path, item_name)
    __make_dirs(dir_path)


def __unzip_file_item(zip_file, item_name, dir_path):
    '''
    解压文件项
    args:
        zip_file: 压缩文件
        item_name: 解压项名称
        dir_path: 解压目录
    '''
    item_names = item_name.split('/')
    if len(item_names) == 1:
        __write_to_file(zip_file, item_name, os.path.join(dir_path, item_name))
    else:
        file_path = os.path.join(dir_path, '/'.join(item_names[0:len(item_names)-1]))
        if __make_dirs(file_path):
            __write_to_file(zip_file, item_name, os.path.join(dir_path, item_name))


def __make_dirs(dir_path):
    '''
    创建目录
    args:
        dir_path: 目录名称
    '''
    try:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        return True
    except Exception as ex:
        return ZipException("dir '{}' already exists.".format(dir_path))


def __write_to_file(zip_file, zip_name, local_file_name):
    '''
    文件项写入文件
    args:
        zip_file: 压缩文件对象
        zip_name: 压缩文件项名称
        local_file_name: 本地文件名称
    '''
    local_file = open(local_file_name, 'wb')
    local_file.write(zip_file.read(zip_name))
    local_file.close()
    return True


if  __name__ == '__main__':
# CZipHelper.zip_folder("/home/pine/dotfile", "/home/pine/dotfile.zip")
# CZipHelper.unzip_to_folder("/home/pine/dotfile.bak", "/home/pine/dotfile.zip")
    print "zip module"
