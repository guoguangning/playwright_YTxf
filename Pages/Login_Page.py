

from playwright.sync_api import sync_playwright
from BasePage.BasePage import BasePage
from BasePage.logger import Logger

logger = Logger("Login_Page").get_log()


class LoginPage(BasePage):
    __path = '/login'
    __username_selector = '//input[@placeholder="请输入账号"]'
    __password_selector = '//input[@placeholder="请输入密码"]'
    __login_button_selector = '//div[@class="loginBox"]/button'

    def goto_login(self):
        try:
            self._goto_url(self.__path)
            logger.info("Navigating to login page")
        except Exception as e:
            logger.error(f"Failed to open login page: {e}")
            raise

    def fill_username(self, value: str) -> None:
        try:
            self._fill(self.__username_selector, value)
            logger.info("Filling in username")
        except Exception as e:
            logger.error(f"Failed to fill username: {e}")
            raise

    def fill_password(self, value: str) -> None:
        try:
            self._fill(self.__password_selector, value)
            logger.info("Filling in password")
        except Exception as e:
            logger.error(f"Failed to fill password: {e}")
            raise

    def click_login_button(self) -> None:
        try:
            self._click(self.__login_button_selector)
            logger.info("Clicking login button")
        except Exception as e:
            logger.error(f"Failed to click login button: {e}")
            raise


# with sync_playwright() as p:
#     __username = '13723945525'
#     __password = 'Th#VHv1P6T3s53Ug'
#     __assert = '//*[@id="app"]/div[1]/div[1]/img'
#     browser = p.chromium.launch(headless=False, args=['--start-maximized'])
#     context = browser.new_context()
#     page = browser.new_page(no_viewport=True)
#     login_page = LoginPage(page)
#     login_page.goto_login()
#     login_page.fill_username(__username)
#     login_page.fill_password(__password)
#     login_page.click_login_button()
#     page.wait_for_timeout(2000)
#     try:
#         assert page.is_visible(__assert)
#         logger.info("Element is visible")
#     except Exception as e:
#         logger.error(f"Element is not visible: {e}")
#         raise
#     context.close()
#     browser.close()
