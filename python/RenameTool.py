#coding=utf-8

import os
import shutil

class FileRenamer(object):

    def __init__(self, prefix = ''):
        self.__prefix = prefix
        self.__index = 0


    def rename_file_in_folder(self, dir_name):
        try:
            for filename in os.listdir(dir_name):
                if os.path.isfile(os.path.join(dir_name, filename)):
                    self.__rename_file(dir_name, filename)
                    self.__index = self.__index + 1
            return True
        
        except Exception, ex:
            print 'FileRenamer: Error in rename_file_in_folder=%s .'%(ex)
            return False


    def __rename_file(self, dir_path, file_name):
        file_ext = file_name[file_name.rfind('.'):]
        new_name = '%s%08d%s'%(self.__prefix, self.__index, file_ext)
        os.rename(os.path.join(dir_path, file_name),
                  os.path.join(dir_path, new_name))


class ImageMover(object):

    def __init__(self, prefix = '', dst_index = 0):
        self.__prefix = prefix
        self.__dst_index = dst_index

    def move(self, src_dir, dir_name):
        try:
            for filename in os.listdir(src_dir):
                if os.path.isfile(os.path.join(src_dir, filename)):
                    self.__move_file(src_dir, filename, dir_name)
                    self.__dst_index = self.__dst_index + 1
            return True
        except Exception, ex:
            print 'ImageMover: Error in move=%s .'%(ex)
            return False

    def __move_file(self, dir_path, file_name, dst_dir):
        try:
            im = Image.open(os.path.join(dir_path, file_name))
            if im.size[0] < 1000 or im.size[1] < 1000:
                return 

            file_ext = file_name[file_name.rfind('.'):]
            new_name = '%s%08d%s'%(self.__prefix, self.__dst_index, file_ext)
            shutil.copyfile(os.path.join(dir_path, file_name), os.path.join(dst_dir, new_name))
        except Exception, ex:
            print 'ImageMover: Error in __move_file=%s .'%(ex)

if __name__ == '__main__':
    f = FileRenamer('')
    #print f.rename_file_in_folder('F:/图片/桌面背景'.decode('utf8'))
    print f.rename_file_in_folder(u'F:/图片/桌面背景')

    # f = ImageMover('', 913)
    # print f.move('G:/BaiduYunDownload/bizhi', u'F:/图片/桌面背景')
    
    print "RenameTool module"
        
                                           
