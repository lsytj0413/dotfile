#coding=utf-8

import os
import sys
import shutil
import time

class UpdateProcessor(object):

    def __init__(self, script_path, conv):
        self.__script_path = script_path
        self.__conv = conv
        self.__app_path = self.__conv.get_app_path()
        self.__backup_path = self.__conv.get_backup_path() + '/appdemo'
        self.__app_name = 'appdemo.exe'
        
    def __stop_app(self):
        #停止应用
        #如果是调用conv的接口处理，则是kill，处理.exe
        try:
            self.__conv.notify_process(1, "process_update: begin to stop the app=%s."%(self.__app_name))
                        
            if 0 == self.__conv.stop_app_by_name(self.__app_path, self.__app_name):
                #停止应用失败
                self.__conv.notify_process(2, "process_update: can't stop the app=%s."%(self.__app_name))
                return False
            
            self.__conv.notify_process(1, "process_update: stop the app success.")
            return True
        except Exception, ex:
            print "Error in stop_app:error=%s"%(ex)
            return False

    def __start_app(self):
        #启动应用
        #如果是调用conv的接口处理，则是create，处理.exe
        try:
            self.__conv.notify_process(1, "process_update: begin to start the app=%s."%(self.__app_name))
            if 0 == self.__conv.start_app_by_name(self.__app_path, self.__app_name):
                #启动应用失败
                self.__conv.notify_process(2, "process_update: can't start the app=%s."%(self.__app_name))
                return False

            self.__conv.notify_process(1, "process_update: start the app success.")
            return True
        except Exception, ex:
            print "Error in start_app:error=%s"(ex)
            return False

    def __backup_app(self):
        #备份应用
        try:
            self.__conv.notify_process(1, "process_update: begin to backup the app=%s."%(self.__app_name))
            
            if not os.path.exists(self.__backup_path + '/data'):
                os.makedirs(self.__backup_path + '/data')
            shutil.copy(self.__app_path + '/appdemo.exe', self.__backup_path)
            shutil.copy(self.__app_path + '/data/data.txt', self.__backup_path + '/data')
            
            self.__conv.notify_process(1, "process_update: backup the app success.")
            return True
        except Exception, ex:
            self.__conv.notify_process(2, "process_update: can't backup the app=%s, error=%s."%(self.__app_name, ex))
            return False

    def __recovery_app(self):
        #恢复应用
        try:
            self.__conv.notify_process(1, "process_update: begin to reconvery the app=%s."%(self.__app_name))

            shutil.copy(self.__backup_path + '/appdemo.exe', self.__app_path)
            shutil.copy(self.__backup_path + '/data/data.txt', self.__app_path + '/data')
            
            self.__conv.notify_process(1, "process_update: recovery the app success.")
            return True
        except Exception, ex:
            self.__conv.notify_process(2, "process_update: can't recovery the app=%s, error=%s."%(self.__app_name, ex))
            return False

    def __update_app(self):
        #升级操作
        try:
            self.__conv.notify_process(1, "process_update: begin to udpate the app=%s."%(self.__app_name))

            shutil.copy(self.__script_path + '/appdemo.exe', self.__app_path)
            shutil.copy(self.__script_path + '/data/data.txt', self.__app_path + '/data')
            
            self.__conv.notify_process(1, "process_update: udpate the app success.")
            return True
        except Exception, ex:
            self.__conv.notify_process(2, "process_update: can't udpate the app=%s, error=%s."%(self.__app_name, ex))
            return False

    def __remove_backup(self):
        #删除备份目录
        try:
            self.__conv.notify_process(1, "process_update: begin to remove the backup.")
            if os.path.exists(self.__backup_path):
                shutil.rmtree(self.__backup_path)

            self.__conv.notify_process(1, "process_update: remove the backup success.")
            return True
        except Exception, ex:
            #删除失败
            self.__conv.notify_process(2, "process_update: can't remove the backup.")
            return False
    
    def do_process_update(self):
        #新的流程示例
        #首先停止应用，如果不能停止的话，只能说。。。。。over了
        try:
            self.__conv.notify_progress(1, 0, 100)
            if False == self.__stop_app():
                return 0
        except Exception, ex:
            #一般来说不可能执行到这里
            print ex
            return 0

        self.__conv.notify_progress(1, 10, 100)
        
        time.sleep(1)
        #可以开始真正的有副作用的流程了
        try:
            #备份应用            
            if False == self.__backup_app():
                #备份失败                
                return 0

            self.__conv.notify_progress(1, 20, 100)
            
            time.sleep(1)
            #升级处理            
            if False == self.__update_app():
                #升级处理失败，尝试恢复应用
                time.sleep(1)
                if False == self.__recovery_app():
                    #恢复失败，不需要尝试重启应用                    
                    return 0
                
            self.__conv.notify_progress(1, 80, 100)
            
            #只需要升级处理与恢复应用中有一个成功，就尝试重启应用
            time.sleep(1)
            if False == self.__start_app():
                #重启应用失败                
                return 0
            
            self.__conv.notify_progress(1, 100, 100)
            return 1
        except Exception, ex:
            #不知道中间哪里出异常了。。。。。。，一般来说需要各个子处理过程中不要抛出异常，因为异常会影响升级失败的恢复过程，因为异常会影响升级失败的恢复过程，只要各个子处理过程不抛出异常，就不会到这来
            print "Critical Error in do_process_update: unexcept error=%s"%(ex)
            return 0
        finally:
            #在处理流程中，不管怎么结束都应该尝试去删除备份目录，如果备份目录存在的话
            self.__remove_backup()
        


def process_update(script_path, conv):
    '''一般包含以下几个动作
    1：停止应用
    2：备份应用
    3：升级处理
    4：重启应用
    5：恢复应用
    '''
    conv.notify_process(1, "process_update: begin to update app.")
    update_processor = UpdateProcessor(script_path, conv)
    return update_processor.do_process_update()


class test_conv(object):
    def notify_process(self, i, j):
        print j
        pass
    def notify_progress(self, i, j, k):
        pass

    def get_app_path(self):
        return 'D:/updatedemo/appdemo'

    def get_backup_path(self):
        return '.'

if __name__ == "__main__":
    process_update('D:/BaiduYunDownload/updatetest', test_conv())
    print 'testadd module'
