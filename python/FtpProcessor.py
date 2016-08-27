#coding=utf-8

from ftplib import FTP


class FtpHelper(object):
    '''
    Ftp 帮助类
    '''

    __ftp_obj = FTP()

    def __init__(self):
        pass

    def connect(self, remote_addr, port):
        try:
            self.__ftp.connect(remote_addr, port, 5)
            return True

        except Exception, ex:
            print "FtpDownloader:Error in connect=%s ."%(ex)
            return False


    def login(self, user_name, user_password):
        try:
            self.__ftp.login(user_name, user_password)
            return True

        except Exception, ex:
            print "FtpDownloader:Error in login=%s ."(ex)
            return False


    def getwelcome(self):
        try:
            return self.__ftp.getwelcome()

        except Exception, ex:
            return "FtpDownloader:Error in getwelcome=%s ."(ex)


    def download_file(self, remote_file_name, local_file_name, conv = None):
        try:
            self.__local_file = open(local_file_name, 'ab+')
            self.__ftp.retrbinary("RETR %s"%(remote_file_name), self.__on_write, 1024)
            return True

        except Exception, ex:
            print "FtpDownloader:Error in download_file=%s ."(ex)
            return False


    def quit(self):
        try:
            self.__ftp.quit()
            return True
        except Exception, ex:
            print "FtpDownloader:Error in quit=%s ."(ex)
            return False

    def __on_write(self, file_data):
        self.__local_file.write(file_data)



if __name__ == "__main__":
    f = FtpDownloader()
    print f.connect('10.0.3.167', 21)
    print f.login('anonymous', '')
    print f.getwelcome()

    print f.download_file('/BaiduYunDownload/Effective_Modern_C++.pdf', 'Effective_Modern_C++.pdf')

    print 'FtpProcessor module'
