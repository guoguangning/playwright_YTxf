"""
-*- coding: utf-8 -*-
@File    : TestLogin.py
@Date    : 2024/9/24 15:25
@Author  : ggn
"""

import pytest
from Pages.Login_Page import LoginPage
from BasePage.logger import Logger
from Utils.Utils_yaml import load_yaml

logger = Logger("TestLogin").get_log()


class TestLogin(object):
    param_data = load_yaml(r'C:\case\playwright-YTxf\TestDatas\PassingData\TestLogin.yaml')
    if param_data is None:
        raise ValueError("无法加载 TestSiteAcceptance.yaml 文件或文件内容为空。")

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('login_data', param_data)
    def test_login(self, page, login_data):
        """测试登录功能"""

        try:
            self.login_page = LoginPage(page)  # 创建 LoginPage 实例
            # 进行登录操作
            self.login_page.goto_login()
            self.login_page.fill_username(login_data['username'])
            self.login_page.fill_password(login_data['password'])
            self.login_page.click_login_button()

            if self.login_page._ele_to_be_expect(login_data['expected']):
                logger.info("登录成功")
        except Exception as e:
            logger.error(f"登录失败: {e}")
            raise


if __name__ == '__main__':
    pytest.main(['-v', __file__])
