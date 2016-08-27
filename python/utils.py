#coding=utf-8

class RaiiObj(object):

    def __init__(self, obj, callback_fn = lambda x: x.close()):
        self.__obj = obj
        self.__callback_fn = callback_fn

    def __del__(self):
        self.__callback_fn(self.__obj)

    def obj(self):
        return self.__obj
            

if __name__ == '__main__':
    print 'utils module'
