"""
-*- coding: utf-8 -*-
@File    : TestRectificationDecisionConfirmation.py
@Date    : 2024/10/12 13:42
@Author  : ggn
"""
import pytest

from BasePage.logger import Logger
from Pages.RectificationDecisionConfirmation_Page import RectificationDecisionConfirmationPage
from Testcases.TestLogin import TestLogin
from Utils.Utils_yaml import load_yaml

logger = Logger("TestRectificationDecisionConfirmation").get_log()


class TestRectificationDecisionConfirmation(object):
    yaml_data = load_yaml(r'C:\case\playwright-YTxf\TestDatas\PassingData\Login.yaml')
    if yaml_data is None:
        raise ValueError("无法加载 TestSiteAcceptance.yaml 文件或文件内容为空。")
    login_data = yaml_data[0]

    param_data = load_yaml(r'C:\case\playwright-YTxf\TestDatas\PassingData\TestRectificationDecisionConfirmation.yaml')
    if param_data is None:
        raise ValueError("无法加载 TestSiteAcceptance.yaml 文件或文件内容为空。")

    @pytest.fixture(autouse=True)
    def set_up(self, page):
        """在每个测试用例前执行"""
        self.login = TestLogin()
        self.login.test_login(page, self.login_data)
        self.test_RectificationDecisionConfirmation = RectificationDecisionConfirmationPage(page)

    @pytest.mark.run(order=9)
    @pytest.mark.parametrize('project_data', param_data)
    def test_rectification_decision_confirmation(self, project_data):
        """
        测试整改判定确认功能
        """
        try:
            self._navigate_to_rectification_decision_confirmation()
            self._submit_rectification_decision_confirmation()
            if self._assert_rectification_decision_confirmation(project_data):
                logger.info('整改判定确认提交成功')
        except Exception as e:
            logger.error(f"整改判定确认提交失败: {e}")
            raise

    def _navigate_to_rectification_decision_confirmation(self):
        self.test_RectificationDecisionConfirmation.goto_rectification_decision_confirmation()
        self.test_RectificationDecisionConfirmation.click_enter_acceptance()
        self.test_RectificationDecisionConfirmation.click_rectification_decision_confirmation()

    def _submit_rectification_decision_confirmation(self):
        self.test_RectificationDecisionConfirmation.submit()

    def _assert_rectification_decision_confirmation(self, project_data):
        try:
            self.test_RectificationDecisionConfirmation._ele_to_be_expect(project_data['expected'])
            return True
        except Exception as e:
            logger.error(f"断言不可见: {e}")
            return False

    @pytest.mark.run(order=12)
    @pytest.mark.parametrize('project_data', param_data)
    def test_rectification_decision_confirmation_2(self, project_data):
        """
        测试整改判定确认功能
        """
        try:
            self._navigate_to_rectification_decision_confirmation_2()
            self._submit_rectification_decision_confirmation_2()
            if self._assert_rectification_decision_confirmation_2(project_data):
                logger.info('整改判定确认提交成功')
        except Exception as e:
            logger.error(f"整改判定确认提交失败: {e}")
            raise

    def _navigate_to_rectification_decision_confirmation_2(self):
        self.test_RectificationDecisionConfirmation.goto_rectification_decision_confirmation()
        self.test_RectificationDecisionConfirmation.click_enter_acceptance()
        self.test_RectificationDecisionConfirmation.click_rectification_decision_confirmation()

    def _submit_rectification_decision_confirmation_2(self):
        self.test_RectificationDecisionConfirmation.submit()

    def _assert_rectification_decision_confirmation_2(self, project_data):
        try:
            self.test_RectificationDecisionConfirmation._ele_to_be_expect(project_data['expected'])
            return True
        except Exception as e:
            logger.error(f"断言不可见: {e}")
            return False

    @pytest.mark.run(order=17)
    @pytest.mark.parametrize('project_data', param_data)
    def test_rectification_decision_confirmation_3(self, project_data):
        """
        测试整改判定确认功能
        """
        try:
            self._navigate_to_rectification_decision_confirmation_3()
            self._submit_rectification_decision_confirmation_3()
            if self._assert_rectification_decision_confirmation_3(project_data):
                logger.info('整改判定确认提交成功')
        except Exception as e:
            logger.error(f"整改判定确认提交失败: {e}")
            raise

    def _navigate_to_rectification_decision_confirmation_3(self):
        self.test_RectificationDecisionConfirmation.goto_rectification_decision_confirmation()
        self.test_RectificationDecisionConfirmation.click_enter_acceptance()
        self.test_RectificationDecisionConfirmation.click_rectification_decision_confirmation()

    def _submit_rectification_decision_confirmation_3(self):
        self.test_RectificationDecisionConfirmation.submit()

    def _assert_rectification_decision_confirmation_3(self, project_data):
        try:
            self.test_RectificationDecisionConfirmation._ele_to_be_expect(project_data['expected'])
            return True
        except Exception as e:
            logger.error(f"断言不可见: {e}")
            return False


if __name__ == '__main__':
    pytest.main(['-s', __file__])
