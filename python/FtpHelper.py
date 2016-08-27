#coding=utf-8

from ftplib import FTP


class CFtpHelper(FTP):
    '''
    Ftp 帮助类
    '''

    def download_file(self, remote_file_name, local_file_name):
        '''
        通过FTP下载文件

        args:
            remote_file_name: 远程文件名称
            local_file_name: 本地文件名称

        return:
            bool: True

        exceptions:
            Error
        '''
        local_file = open(local_file_name, 'ab+')
        self.__ftp.retrbinary("RETR %s"%(remote_file_name), local_file.write, 1024)
        return True


if __name__ == "__main__":
    print 'FtpHelper module'
