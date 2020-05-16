import smtplib
from email.header import Header
from email.mime.text import MIMEText

import win32clipboard as w
import win32con
import win32gui

import Global_Config

class Notice_Method:
    from_addr = Global_Config.from_addr
    password = Global_Config.password
    to_addr = Global_Config.to_addr
    smtp_server = Global_Config.smtp_server
    Email_Header=Global_Config.Email_Header

    QQ_Name=Global_Config.QQ_Name
    send_method=Global_Config.Not_Met

    def send_email(self,msg):
        msg = MIMEText(msg)
        msg['From'] = Header(self.from_addr)
        msg['To'] = Header(self.to_addr)
        msg['Subject'] = Header(self.Email_Header)
        server = smtplib.SMTP_SSL(host=self.smtp_server)
        server.connect(self.smtp_server, 465)

        server.login(self.from_addr, self.password)
        server.sendmail(self.from_addr, self.to_addr, msg.as_string())
        server.quit()

    def send_QQmessage(self,msg):
        # 窗口名字，就是备注名
        name = self.QQ_Name
        # 将测试消息复制到剪切板中
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
        w.CloseClipboard()
        # 获取窗口句柄
        handle = win32gui.FindWindow(None, name)
        # 填充消息
        win32gui.SendMessage(handle, 770, 0, 0)
        # 回车发送消息
        win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)

    def Select_Method(self,msg):
        if self.send_method.upper() =='QQ':
            self.send_QQmessage(msg)
        elif self.send_method.upper() =='EMAIL':
            self.send_email(msg)
        else:
            print("输入错误,请重新启动程序")




