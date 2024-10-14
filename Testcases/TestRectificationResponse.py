"""
-*- coding: utf-8 -*-
@File    : TestRectificationResponse.py
@Date    : 2024/10/11 15:10
@Author  : ggn
"""
import pytest

from BasePage.logger import Logger
from Pages.RectificationResponse_Page import RectificationResponsePage
from Testcases.TestLogin import TestLogin
from Utils.Utils_yaml import load_yaml

logger = Logger("TestRectificationResponse").get_log()


class TestRectificationResponse(object):
    yaml_data = load_yaml(r'C:\case\playwright-YTxf\TestDatas\PassingData\Login.yaml')
    if yaml_data is None:
        raise ValueError("无法加载 TestSiteAcceptance.yaml 文件或文件内容为空。")
    login_data = yaml_data[1]

    param_data = load_yaml(r'C:\case\playwright-YTxf\TestDatas\PassingData\TestRectificationResponse.yaml')
    if param_data is None:
        raise ValueError("无法加载 TestSiteAcceptance.yaml 文件或文件内容为空。")

    @pytest.fixture(autouse=True)
    def set_up(self, page):
        """在每个测试用例前执行"""
        self.login = TestLogin()
        self.login.test_login(page, self.login_data)
        self.test_RectificationResponse = RectificationResponsePage(page)

    @pytest.mark.run(order=7)
    @pytest.mark.parametrize('project_data', param_data)
    def test_rectification_response(self, project_data):
        """
        测试整改回复1-1功能
        """
        try:
            self._navigate_to_rectification_response()
            self._select_input_response(project_data)
            self._submit_rectification_response()
            if self._assert_rectification_response(project_data):
                logger.info('整改回复提交成功')
        except Exception as e:
            logger.error(f"整改回复提交失败: {e}")
            raise

    def _navigate_to_rectification_response(self):
        self.test_RectificationResponse.goto_rectification_response()
        self.test_RectificationResponse.click_enter_acceptance()
        self.test_RectificationResponse.click_rectification_response()

    def _select_input_response(self, project_data):
        self.test_RectificationResponse.input_reply(project_data['value'], project_data['files'])

    def _submit_rectification_response(self):
        self.test_RectificationResponse.submit()

    def _assert_rectification_response(self, project_data):
        try:
            self.test_RectificationResponse._ele_to_be_expect(project_data['expected'])
            return True
        except Exception as e:
            logger.error(f"断言不可见: {e}")
            return False

    @pytest.mark.run(order=10)
    @pytest.mark.parametrize('project_data', param_data)
    def test_rectification_response_2(self, project_data):
        """
        测试整改回复1-2功能
        """
        try:
            self._navigate_to_rectification_response_2()
            self._select_input_response_2(project_data)
            self._submit_rectification_response_2()
            if self._assert_rectification_response_2(project_data):
                logger.info('整改回复提交成功')
        except Exception as e:
            logger.error(f"整改回复提交失败: {e}")
            raise

    def _navigate_to_rectification_response_2(self):
        self.test_RectificationResponse.goto_rectification_response()
        self.test_RectificationResponse.click_enter_acceptance()
        self.test_RectificationResponse.click_rectification_response()

    def _select_input_response_2(self, project_data):
        self.test_RectificationResponse.input_reply_2(project_data['value2'])

    def _submit_rectification_response_2(self):
        self.test_RectificationResponse.submit()

    def _assert_rectification_response_2(self, project_data):
        try:
            self.test_RectificationResponse._ele_to_be_expect(project_data['expected'])
            return True
        except Exception as e:
            logger.error(f"断言不可见: {e}")
            return False

    @pytest.mark.run(order=15)
    @pytest.mark.parametrize('project_data', param_data)
    def test_rectification_response_3(self, project_data):
        """
        测试整改回复2-1功能
        """
        try:
            self._navigate_to_rectification_response_3()
            self._select_input_response_3(project_data)
            self._submit_rectification_response_3()
            if self._assert_rectification_response_3(project_data):
                logger.info('整改回复提交成功')
        except Exception as e:
            logger.error(f"整改回复提交失败: {e}")
            raise

    def _navigate_to_rectification_response_3(self):
        self.test_RectificationResponse.goto_rectification_response()
        self.test_RectificationResponse.click_enter_acceptance()
        self.test_RectificationResponse.click_rectification_response()

    def _select_input_response_3(self, project_data):
        self.test_RectificationResponse.input_reply_3(project_data['value3'], project_data['value'])

    def _submit_rectification_response_3(self):
        self.test_RectificationResponse.submit()

    def _assert_rectification_response_3(self, project_data):
        try:
            self.test_RectificationResponse._ele_to_be_expect(project_data['expected'])
            return True
        except Exception as e:
            logger.error(f"断言不可见: {e}")
            return False


if __name__ == '__main__':
    pytest.main(['-s', __file__])
