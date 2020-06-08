#导入安装库
import pymysql
import requests
import re
import time
import Global_Config
import Notice_Method


class GetPrice:
    def __init__(self,new_Not_M):
        self.new_Not_M = new_Not_M
    #class属性
    header = Global_Config.header
    url = Global_Config.url

    db_table = Global_Config.db_table
    db_host = Global_Config.db_host
    db_port = Global_Config.db_port
    db_user = Global_Config.db_user
    db_password = Global_Config.db_password
    db_name = Global_Config.db_name

    db_connect = pymysql.connect(host=db_host, port=db_port, user=db_user, password=db_password, db=db_name)
    cursor = db_connect.cursor()
    Monitor_Key = Global_Config.Monitor_Key


    def Monitor_Price_WriteDB(self):
        if (self.table_exists(self.cursor,self.db_table) != 1):
            print("对应表在数据库中不存在，正在创建...")
            sql_Create_Table = 'create table ' + self.db_table + '(article_date varchar(255) not null,article_title varchar(255) not null PRIMARY KEY,article_price varchar(255) not null,article_url varchar(255) not null,article_mall varchar(255) not null,article_timesort int(255) not null)'
            #sql_Create_Table='create table '+self.db_table+'(time varchar(255) not null,title varchar(255) not null PRIMARY KEY,timesort int(255) not null)'
            self.cursor.execute(sql_Create_Table)
            self.db_connect.commit()
            print('{}创建完成，开始将数据写入表中...'.format(self.db_table))
        else:
            print("{}在数据库中已存在，开始将数据写入表中...".format(self.db_table))


    def table_exists(self,cursor, table_name):
        sql = "show tables;"
        cursor.execute(sql)
        tables = [cursor.fetchall()]
        table_list = re.findall('(\'.*?\')', str(tables))
        table_list = [re.sub("'", '', each) for each in table_list]
        if table_name in table_list:
            return 1
        else:
            return 0


    def get_json(self,timesort, timesort2):
        sql_data=[]
        if timesort <= timesort2 - 300:
            print('程序已经爬取5分钟之内的全部数据，已暂时停止，等待下次爬取...')
            return
        else:

            params = {
                'type': 'a',
                'timesort': timesort
            }
            response = requests.get(self.url, headers=self.header, params=params)
            response_json_data = response.json()
            print('当前爬取的时间戳为{},当前时间的时间戳为{}'.format(timesort, timesort2))
            try:

                for json_data in response_json_data:
                    article_date = json_data.get('article_date')
                    article_title = json_data.get('article_title')
                    article_price = json_data.get('article_price')
                    article_url = json_data.get('article_url')
                    article_mall = json_data.get('article_mall')
                    article_timesort = json_data.get('timesort')
                    sql_data = [article_date, article_title, article_price,article_url,article_mall,article_timesort]
                    sql = 'insert into ' +self.db_table+ ' values(%s, %s, %s, %s, %s, %s)'
                    self.cursor.execute(sql, sql_data)
                    self.db_connect.commit()
                    print(sql_data)
                    for key in self.Monitor_Key:
                        if sql_data[1].find(key) > -1:
                            #with open('test.txt','a+') as f:
                                #f.write(str(sql_data)+'\n')
                            self.new_Not_M.Select_Method(str(sql_data))
                            break
                self.get_json(sql_data[5], timesort2)
            except pymysql.err.IntegrityError as f:
                print('由于{}已经在数据库中存在，爬虫已暂时停止，等待下次爬取...'.format(sql_data[1]))
                return


def main():
    new_Not_M = Notice_Method.Notice_Method()
    m1 = GetPrice(new_Not_M)
    m1.Monitor_Price_WriteDB()
    try:
        con = 0
        while con >= 0:
            con += 1
            print('当前时间:{},循环第{}次，已经运行{}秒'.format(time.strftime('%Y-%m-%d %H:%M:%S'), con, (con - 1) * Global_Config.Cycle_time))
            m1.get_json(int(time.time()), int(time.time()))
            time.sleep(Global_Config.Cycle_time)
    except Exception as f:
        new_Not_M.Select_Method("程序由于意外已停止运行,报错原因为{}，{},{}".format(f,f.__traceback__.tb_lineno,f.__traceback__.tb_frame.f_globals['__file__']))
        print(f)




if __name__ == '__main__':
    main()