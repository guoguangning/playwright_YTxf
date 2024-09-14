from typing import Optional, Union, List
from playwright.sync_api import expect, Page, Locator
from BasePage.logger import Logger
from Utils.Utils import Utils

logger = Logger("BasePage").get_log()


class BasePage:

    def __init__(self, page: Page):
        self.page = page
        self.utils = Utils()

    def _goto_url(self, path: str) -> None:
        """使用配置文件中的 URL 打开网页"""
        full_url = self.utils.get_full_url(path)
        try:
            self.page.goto(full_url)
            logger.info(f"Navigated to URL: {full_url}")
        except Exception as e:
            logger.error(f"Cannot navigate to page: {e}")

    def _click(self, locator: str, frame_locator: Optional[str] = None) -> None:
        """
        点击元素
        :param locator: 传入元素定位器
        :param frame_locator: 传入frame框架的的定位器，如果没有传入，则一般点击
        :return:
        """
        try:
            target = self._get_target_locator(locator, frame_locator)
            target.click()
        except Exception as e:
            logger.error(f"点击失败: {e}")

    def _hover(self, locator: str, frame_locator: Optional[str] = None) -> None:
        """
        悬停在元素上
        :param locator: 传入元素定位器
        :param frame_locator: 传入frame框架的的定位器，如果没有传入，则一般悬停
        :return:
        """
        try:
            target = self._get_target_locator(locator, frame_locator)
            target.hover()
        except Exception as e:
            logger.error(f"悬停失败: {e}")

    def _fill(self, locator: str, value: str, frame_locator: Optional[str] = None) -> None:
        """
        定位元素，输入内容
        :param locator:传入元素定位器
        :param value:传入输入的值
        :param frame_locator: 传入frame框架
        :return:
        """
        try:
            target = self._get_target_locator(locator, frame_locator)
            target.fill(value)
        except Exception as e:
            logger.error(f"输入失败: {e}")

    def _type(self, locator: str, value: str, frame_locator: Optional[str] = None) -> None:
        """
        模拟人工输入，一个键一个键的输入
        :param locator:传入元素定位器
        :param value:传入输入的值
        :param frame_locator: 传入frame框架
        :return:
        """
        try:
            target = self._get_target_locator(locator, frame_locator)
            target.type(text=value, delay=100)
        except Exception as e:
            logger.error(f"输入失败: {e}")

    def _file(self, locator: str, files: Union[str, List[str]], frame_locator: Optional[str] = None) -> None:
        """
        上传文件的方法
        :param locator: 定位器
        :param files: 单个文件名，或者列表存放多个文件
        :param frame_locator: iframe框架定位器，如果没有就不传
        :return:
        """
        try:
            target = self._get_target_locator(locator, frame_locator)
            target.set_input_files(files)
        except Exception as e:
            logger.error(f"文件上传失败: {e}")

    def _ele_to_be_visible(self, locator: str) -> bool:
        """断言元素可见，并记录日志"""
        try:
            # 日志记录尝试断言的元素定位器
            logger.info(f"Attempting to assert that the element with locator '{locator}' is visible.")

            # 断言元素可见
            is_visible = expect(self.page.locator(locator)).to_be_visible()

            # 日志记录断言结果
            if is_visible:
                logger.info(f"Element with locator '{locator}' is visible.")
            else:
                logger.warning(f"Element with locator '{locator}' is not visible.")

            return is_visible
        except Exception as e:
            # 日志记录异常情况
            logger.error(f"An error occurred while asserting visibility of element with locator '{locator}': {e}")
            return False

    def _ele_to_be_visible_force(self, locator: str, frame_locator: Optional[str] = None, timeout: int = 5) -> None:
        """强制等待某个元素可见"""
        target = self._get_target_locator(locator, frame_locator)
        for _ in range(timeout * 2):  # 每0.5秒检查一次
            self.page.wait_for_timeout(500)
            if target.is_visible():
                return
        raise Exception("元素未找到!")

    def _ele_is_checked(self, locator: str) -> bool:
        """判断元素是否被选选中"""
        return self.page.is_checked(locator)

    def _browser_operation(self, reload: bool = False, forward: bool = False, back: bool = False) -> None:
        """浏览器操作，reload 刷新，forward 前进，back 后退"""
        if reload:
            self.page.reload()
        if back:
            self.page.go_back()
        if forward:
            self.page.go_forward()

    def screenshot(self, path: str, full_page: bool = True, locator: Optional[str] = None) -> str:
        """截图功能，默认截取全屏，如果传入定位器表示截取元素"""
        if locator:
            self.page.locator(locator).screenshot(path=path)
        else:
            self.page.screenshot(path=path, full_page=full_page)
        return path

    def _get_target_locator(self, locator: str, frame_locator: Optional[str] = None) -> Locator:
        """获取目标定位器"""
        if frame_locator:
            return self.page.frame_locator(frame_locator).locator(locator)
        return self.page.locator(locator)
