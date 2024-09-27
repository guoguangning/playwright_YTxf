# TestLogin.py

import pytest
from Pages.Login_Page import LoginPage
from BasePage.logger import Logger

logger = Logger("TestLogin").get_log()


class TestLogin(object):
    login_data = [
        ('13723945525', 'Th#VHv1P6T3s53Ug', '//*[@id="app"]/div[1]/div[1]/img')
    ]

    @pytest.mark.parametrize('username, password, expected', login_data)
    def test_login(self, page, username, password, expected):
        """测试登录功能"""
        login_page = LoginPage(page)  # 创建 LoginPage 实例

        # 进行登录操作
        login_page.goto_login()
        login_page.fill_username(username)
        login_page.fill_password(password)
        login_page.click_login_button()
        try:
            login_page._ele_to_be_visible(expected)
            logger.info("assert is visible")
        except Exception as e:
            logger.error(f"assert is not visible: {e}")
            raise


if __name__ == '__main__':
    pytest.main(['-v', __file__])
