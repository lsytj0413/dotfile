#coding=utf-8


WalkType = {
    'File': 0,
    'Directory': 1,
    'All': 2
}


def walk(type):
    def walk_imp(fn):
        def walk_wrapper(dir_path):
            import os
            import sys
            for file_name in os.listdir(dir_path):
                file_path = os.path.join(dir_path, file_name)
                if type == WalkType['All']:
                    fn(file_path)
                elif type == WalkType['File'] and \
                     os.path.isfile(file_path):
                    fn(file_path)
                elif type == WalkType['Directory'] and \
                     os.path.isdir(file_path):
                    fn(file_path)
        return walk_wrapper
    return walk_imp


if __name__ == '__main__':
    print 'DirWalker module'
