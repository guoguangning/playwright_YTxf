import pytest
from playwright.sync_api import sync_playwright

from BasePage.logger import Logger
from Pages.Login_Page import LoginPage

logger = Logger("TestLogin").get_log()


@pytest.fixture(scope="function")
def browser_context():
    """启动 Playwright 浏览器上下文"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=['--start-maximized'])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        yield page
        context.close()
        browser.close()


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
