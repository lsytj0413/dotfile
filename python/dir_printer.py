#coding=utf-8

import os

class DirPrinter(object):

    def __init__(self):
        pass

    def on_file(self, dir_path, file_name):
        # print "file: ", os.path.join(dir_path, file_name)
        pass

    def on_dir(self, dir_path, file_name):
        if file_name.find(".git") != -1:
            print "dir : ", os.path.join(dir_path, file_name)

    def is_recursion(self, dir_path):
        return True

if __name__ == "__main__":
    from dir_walker import dir_walker
    dir_walker(DirPrinter(), "F:/emacs/.spacemacs.d/tools")
    
