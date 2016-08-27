#coding=utf-8

import os
import zipfile


class ZipProcessor(object):

    def __init__(self, zip_file_name, target_dir):
        '''构造对象。

        args:
            zip_file_name：生成的压缩文件的路径名称。
            target_dir：文件夹
        '''
        self.__zip_file_name = zip_file_name
        self.__target_dir = os.path.realpath(target_dir).replace('\\', '/')
        

    def zip_folder(self):
        '''压缩文件夹.

        returns:
            bool值。压缩成功返回True，否则返回False。
        '''
        try:
            zip_file = zipfile.ZipFile(self.__zip_file_name, 'w', zipfile.ZIP_DEFLATED)
        except Exception, ex:
            print 'ZipProcessor: Error in zip_folder=%s .'%(ex)
            return False
        
        try:
            parent_dirs = [os.path.split(self.__target_dir)[1]]
            self.__zip_folder(zip_file, parent_dirs, self.__target_dir)
            
            return True
        except Exception, ex:
            print 'ZipProcessor: Error in zip_folder=%s .'%(ex)
            return False
        finally:
            zip_file.close()


    def __zip_folder(self, zip_file, parent_dirs, current_dir):
        #添加文件夹项
        zip_file.writestr('/'.join(parent_dirs) + '/', '')

        #遍历文件夹
        for filename in os.listdir(current_dir):
            full_file_name = os.path.join(current_dir, filename)
            if os.path.isdir(full_file_name):
                #遍历到文件夹，递归zip
                parent_dirs.append(filename)
                self.__zip_folder(zip_file, parent_dirs, full_file_name)
            else:
                #遍历到文件，压入zip
                zip_name = '/'.join(parent_dirs) + '/' + filename
                zip_file.write(full_file_name, zip_name)

        parent_dirs.pop()


    def unzip_to_folder(self):
        '''解压缩到文件夹。

        returns:
            bool值。解压缩成功返回True，否则返回False。
        '''
        try:
            zip_file = zipfile.ZipFile(self.__zip_file_name, 'r')
        except Exception, ex:
            print 'ZipProcessor: Error in unzip_to_folder=%s .'%(ex)
            return False
        
        try:
            for zip_name in zip_file.namelist():                
                zip_name = zip_name.replace('\\', '/')
                if zip_name.endswith('/'):
                    #是目录项
                    self.__unzip_folder_item(zip_file, zip_name)
                    continue

                #文件项
                self.__unzip_file_item(zip_file, zip_name)
            return True
        
        except Exception, ex:
            print 'ZipProcessor: Error in unzip_to_folder=%s .'%(ex)
            return False
        finally:
            zip_file.close()


    def __unzip_folder_item(self, zip_file, item_name):
        dir_path = os.path.join(self.__target_dir, item_name)
        if not self.__make_dirs(dir_path):
            raise Exception, "can't make-dir=%s ."%(dir_path)

    def __unzip_file_item(self, zip_file, item_name):
        item_names = item_name.split('/')
        if 1 == len(item_names):
            self.__write_to_file(zip_file, item_name, os.path.join(self.__target_dir, item_name))
        else:
            file_path = os.path.join(self.__target_dir, '/'.join(item_names[0:len(item_names)-1]))
            if self.__make_dirs(file_path):
                self.__write_to_file(zip_file, item_name, os.path.join(self.__target_dir, item_name))

        
    def __make_dirs(self, dir_path):
        try:
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

            return True
        except Exception, ex:
            return False


    def __write_to_file(self, zip_file, zip_name, local_file_name):
        local_file = open(local_file_name, 'wb')
        local_file.write(zip_file.read(zip_name))
        local_file.close()
        return True


if __name__ == '__main__':
    zip_processor1 = ZipProcessor('zip.zip', 'zip')
    print zip_processor1.zip_folder()
    zip_processor = ZipProcessor('zip.zip', 'zip1')
    print zip_processor.unzip_to_folder()
    print "zip module"
