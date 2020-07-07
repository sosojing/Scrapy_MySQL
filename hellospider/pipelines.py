# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

#连接数据库
def dbHandle():
    conn = pymysql.connect(
        host = "localhost",
        user = "root",
        passwd = "123",
        charset = "utf8",
        use_unicode = False
    )
    return conn


class HellospiderPipeline:
    def process_item(self, item, spider):
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        cursor.execute("USE tieba")
        # 插入数据库
        sql = "INSERT INTO articles(title,author,reply) VALUES(%s,%s,%s)"
        try:
            cursor.execute(sql,
                           (item['title'], item['author'], item['reply']))
            cursor.connection.commit()
        except BaseException as e:
            print("错误在这里>>>>>>>>>>>>>", e, "<<<<<<<<<<<<<错误在这里")
            dbObject.rollback()
        return item

