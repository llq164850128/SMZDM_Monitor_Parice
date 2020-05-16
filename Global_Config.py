#数据库配置
db_host =""
db_port=3306
db_user="root"
db_password=""
db_name ="SMZDM"      #需要自己新建一个数据库
db_table='SMZDM_Price' #自行命名，如果不存在。程序会自动创建


#邮件提醒方式参数配置
from_addr = '' #发送邮箱
password = ''   #发送密码
to_addr = ''   #接收邮箱
smtp_server = 'smtp.qq.com'     #发送邮件服务器
Email_Header = ''  #邮件标题
#QQ提醒方式参数配置
QQ_Name = ''   #设置接收的QQ好友的昵称或者备注


#监控关键词
Monitor_Key=['男','饮料']    #可以设置多个关键词


#设置爬取的页面参数
header ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    'Connection': 'close'
}    #一般情况下无需修改
url = 'https://faxian.smzdm.com/json_more?'  #一般情况下无需修改


#设置提醒的方法
Not_Met='Email' #可以选择Email或者QQ

#设置循环爬取的时间间隔
Cycle_time=30  #以秒计算，最好不要超过5分钟，否则可能会出现爬取不完整