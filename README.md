# SMZDM_Monitor_Parice
python可以实时监控什么值得买最新更新的好价，并根据关键词推送到邮箱或者QQ

如需运行该脚本，需要以下几项准备工作：
1.安装运行以下支持库：
pymysql
requests
pywin32   


Pywin32为windows下操作gui的库，用于QQ方式发送推送消息，如在linux系统下运行该脚本，则无法选择QQ推送方式，且可能需要在Notice_Method下注释掉相关的三个库
import win32clipboard as w
import win32con
import win32gui

2.安装并创建一个用于该脚本的MySql数据库，具体的表可以不用创建，脚本会判断是否存在指定表，如果不存在则会自动创建，推荐使用docker生成数据库，方便快捷，
提供Docker运行MySql命令如下，也可以自行查看Docker Hub
sudo docker run -d -p 3306:3306 -v /mysql:/var/lib/mysql --name mysql -e MYSQL_ROOT_PASSWORD=[自定义密码] mysql:[缺省或填写指定版本]

3.推荐采用邮件方式接收推送，发信邮箱需要开通stmp/pop发信服务，配置中的发送邮箱密码需要填写开通时申请到的密码，QQ邮箱开通服务在 设置——账户 下，
QQ接收方式需要在windows电脑下安装QQ或者Tim来实现，且要把推送的人的聊天窗口打开并保证鼠标指针激活在该QQ或者TIM上

4.将三个脚本放在同一目录下，所有配置信息均在Global_Config下，根据实际需求，填写配置后即可运行SMZDM_Fin_JSON_Price脚本
