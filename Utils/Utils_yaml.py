"""
-*- coding: utf-8 -*-
@File    : Utils_yaml.py
@Date    : 2024/9/27 15:25
@Author  : ggn
"""
import os
import yaml
from BasePage.logger import Logger

logger = Logger("Utils_yaml").get_log()


def load_yaml(file_path):
    """加载YAML文件并返回内容

    参数:
        file_path (str): YAML文件的路径

    返回:
        dict: 加载的YAML内容，若文件不存在或出错则返回 None

    异常:
        yaml.YAMLError: 如果YAML格式不正确
    """

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            dict_value = yaml.load(file.read(), Loader=yaml.FullLoader)
            logger.info(f"成功加载文件 {file_path}。")
            return dict_value
    except yaml.YAMLError as exc:
        logger.error(f"YAML解析错误: {exc}")
        return None


def save_yaml(data, file_path):
    """将数据保存到YAML文件

    参数:
        data (dict): 要保存的数据
        file_path (str): 文件保存路径

    异常:
        IOError: 如果写入文件时出错
    """
    if not os.path.isfile(file_path):
        logger.info(f"文件 {file_path} 不存在，正在创建...")
        return create_yaml(file_path)  # 如果文件不存在，调用 create_yaml 创建文件

    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            yaml.dump(data, file, default_flow_style=False, allow_unicode=True)
            logger.info(f"数据已成功保存至 {file_path}。")
    except IOError as e:
        logger.error(f"写入文件时出错: {e}")


def create_yaml(file_path, default_data=None):
    """创建YAML文件并写入默认数据

    参数:
        file_path (str): 文件路径
        default_data (dict, 可选): 默认数据，默认为空字典
    """
    if default_data is None:
        default_data = {}  # 如果没有提供默认数据则使用空字典

    os.makedirs(os.path.dirname(file_path), exist_ok=True)  # 确保目录存在
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            yaml.dump(default_data, file, default_flow_style=False, allow_unicode=True)
        logger.info(f"文件 {file_path} 创建成功。")
    except IOError as e:
        logger.error(f"创建文件时出错: {e}")


# 以下代码是使用示例，实际使用时可以根据需要调用这些函数
if __name__ == "__main__":
    sample_data = {
        'name': 'Infinity AI',
        'version': '1.0.0',
        'description': 'A chat assistant'
    }
    # 尝试加载数据，如果文件不存在则创建
    loaded_data = load_yaml(r'C:\case\playwright-ytxf\TestDatas\EleData\ed_login.yaml')
    print(loaded_data['__path'])  # 打印加载的内容
