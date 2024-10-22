"""
-*- coding: utf-8 -*-
@File    : Util_mysql.py
@Date    : 2024/10/22 8:35
@Author  : ggn
"""
import configparser
from contextlib import contextmanager
import mysql.connector
from mysql.connector import Error
from BasePage.logger import Logger

logger = Logger("Util_mysql").get_log()


class MySQLConnection:
    """MySQL数据库的连接及相关操作"""

    def __init__(self, config_file=r"C:\case\playwright-YTxf\Config.ini"):
        """
        :param config_file: 配置文件路径
        """
        self.config = self._load_config(config_file)
        self._validate_config()
        self.connection = None
        self.cursor = None

    @staticmethod
    def _load_config(config_file):
        """加载配置文件"""
        config = configparser.ConfigParser()
        config.read(config_file, encoding='utf-8')
        return config

    def _validate_config(self):
        """验证配置文件中的必要选项"""
        if not self.config.has_section('mysql'):
            raise KeyError("Section 'mysql' is missing from the config file.")
        required_keys = ['host', 'port', 'database', 'user', 'password']
        for key in required_keys:
            if not self.config.has_option('mysql', key):
                raise KeyError(f"Key '{key}' is missing from the 'mysql' section.")

    @contextmanager
    def get_cursor(self):
        """上下文管理器用于管理游标的获取和释放"""
        try:
            self.connection = mysql.connector.connect(
                host=self.config['mysql']['host'],
                port=self.config['mysql']['port'],
                database=self.config['mysql']['database'],
                user=self.config['mysql']['user'],
                password=self.config['mysql']['password']
            )
            self.cursor = self.connection.cursor()
            logger.info("数据库连接成功")
            yield self.cursor
        except Error as e:
            logger.error(f"连接时出现错误: {e}")
            raise
        finally:
            self.close_resources()

    def close_resources(self):
        """关闭游标和数据库连接"""
        if self.cursor:
            self.cursor.close()
            logger.info("游标已关闭")
        if self.connection:
            self.connection.close()
            logger.info("数据库连接已关闭")

    def execute_query(self, query):
        """执行 INSERT、UPDATE、DELETE 语句"""
        with self.get_cursor() as cursor:
            try:
                cursor.execute(query)
                self.connection.commit()
                logger.info(f"sql已成功执行: {query}")
            except Error as e:
                self.connection.rollback()
                logger.error(f"执行sql时出现错误: {e}; sql: {query}")
                logger.error("事务已回滚")
                raise

    def execute_read_query(self, query):
        """执行 SELECT 查询"""
        with self.get_cursor() as cursor:
            try:
                cursor.execute(query)
                result = cursor.fetchall()
                logger.info(f"成功读取查询结果: {query}")
                return result
            except Error as e:
                logger.error(f"读取查询时出现错误: {e}; sql: {query}")
                raise


# 示例使用
if __name__ == "__main__":
    # 创建连接对象
    connection_obj = MySQLConnection()

    # 执行语句
    update_query = """
        UPDATE yt_project_check_acceptance
        SET construction_org_code = '1244'
        WHERE
    	construction_org_name = '滨州建设单位3210' 
        """
    try:
        connection_obj.execute_query(update_query)
    except Exception as e:
        logger.error(f"执行更新操作失败: {e}")
