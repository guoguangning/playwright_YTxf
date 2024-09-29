"""
-*- coding: utf-8 -*-
@File    : Utils_url.py
@Date    : 2024/9/24 15:25
@Author  : ggn
"""
import configparser
from urllib.parse import urljoin
from BasePage.logger import Logger

logger = Logger("Utils_url").get_log()


class Utils:
    def __init__(self, config_file_path=r'C:\case\playwright-ytxf\config.ini'):
        self.base_url = self.get_url_from_config(config_file_path)

    def get_full_url(self, path: str) -> str:
        """拼接 base_url 和 path，返回完整的 URL"""
        if not self.base_url:
            logger.error("Base URL is not set. Cannot create full URL.")
            raise ValueError("Base URL is not set.")
        return urljoin(self.base_url, path)

    @classmethod
    def get_url_from_config(cls, config_file_path):
        """
        从配置文件中获取 URL。

        :param config_file_path: 配置文件的路径
        :return: 配置文件中获取的 URL，如果失败则返回 None
        """
        config = configparser.ConfigParser()
        try:
            config.read(config_file_path, encoding='utf-8')
            if not config.has_section('testServer'):
                raise KeyError("Section 'testServer' is missing from the config file.")
            if not config.has_option('testServer', 'url'):
                raise KeyError("Key 'url' is missing from the 'testServer' section.")

            url = config.get('testServer', 'url')
            logger.info(f"Retrieved URL from config: {url}")
            return url
        except (configparser.Error, KeyError) as e:
            logger.error(f"Configuration error: {e}")
        except Exception as e:
            logger.error(f"Failed to retrieve URL from config: {e}")
        return None


# 示例用法
if __name__ == '__main__':
    utils_instance = Utils()

    # 拼接路径，获取完整 URL
    full_url = utils_instance.get_full_url("/login")
    print(full_url)
