"""
-*- coding: utf-8 -*-
@File    : TestAcceptanceConfirmation.py
@Date    : 2024/10/10 16:41
@Author  : ggn
"""
import pytest
from BasePage.logger import Logger
from Pages.AcceptanceConfirmation_Page import AcceptanceConfirmationPage
from Testcases.TestLogin import TestLogin
from Utils.Utils_yaml import load_yaml

logger = Logger("TestAcceptanceConfirmation").get_log()


class TestAcceptanceConfirmation(object):
    yaml_data = load_yaml(r'C:\case\playwright-YTxf\TestDatas\PassingData\Login.yaml')
    if yaml_data is None:
        raise ValueError("无法加载 TestSiteAcceptance.yaml 文件或文件内容为空。")
    login_data = yaml_data[0]

    param_data = load_yaml(r'C:\case\playwright-YTxf\TestDatas\PassingData\TestAcceptanceConfirmation.yaml')
    if param_data is None:
        raise ValueError("无法加载 TestSiteAcceptance.yaml 文件或文件内容为空。")

    @pytest.fixture(autouse=True)
    def set_up(self, page):
        """在每个测试用例前执行"""
        self.login = TestLogin()
        self.login.test_login(page, self.login_data)
        self.test_acceptance_confirmation = AcceptanceConfirmationPage(page)

    @pytest.mark.run(order=5)
    @pytest.mark.parametrize('project_data', param_data)
    def test_acceptance_confirmation(self, project_data):
        """
        测试人员现场验收确认功能
        """
        try:
            self._navigate_to_acceptance_confirmation()
            self._submit_acceptance_conclusion()
            if self._assert_acceptance_conclusion(project_data):
                logger.info('现场验收确认提交成功')
        except Exception as e:
            logger.error(f"现场验收确认提交失败: {e}")
            raise

    def _navigate_to_acceptance_confirmation(self):
        """导航到现场验收结论确认页面"""
        self.test_acceptance_confirmation.goto_site_acceptance()
        self.test_acceptance_confirmation.click_enter_acceptance()
        self.test_acceptance_confirmation.click_site_acceptance()

    def _submit_acceptance_conclusion(self):
        """提交现场验收结论"""
        self.test_acceptance_confirmation.submit()

    def _assert_acceptance_conclusion(self, project_data):
        try:
            self.test_acceptance_confirmation._ele_to_be_expect(project_data['expected'])
            return True
        except Exception as e:
            logger.error(f"断言不可见: {e}")
            return False

    @pytest.mark.run(order=14)
    @pytest.mark.parametrize('project_data', param_data)
    def test_acceptance_confirmation_2(self, project_data):
        """
        测试人员现场验收确认功能
        """
        try:
            self._navigate_to_acceptance_confirmation_2()
            self._submit_acceptance_conclusion_2()
            if self._assert_acceptance_conclusion_2(project_data):
                logger.info('第二次现场验收确认提交成功')
        except Exception as e:
            logger.error(f"第二次现场验收确认提交失败: {e}")
            raise

    def _navigate_to_acceptance_confirmation_2(self):
        """导航到现场验收结论确认页面"""
        self.test_acceptance_confirmation.goto_site_acceptance()
        self.test_acceptance_confirmation.click_enter_acceptance()
        self.test_acceptance_confirmation.click_site_acceptance()

    def _submit_acceptance_conclusion_2(self):
        """提交现场验收结论"""
        self.test_acceptance_confirmation.submit()

    def _assert_acceptance_conclusion_2(self, project_data):
        try:
            self.test_acceptance_confirmation._ele_to_be_expect(project_data['expected'])
            return True
        except Exception as e:
            logger.error(f"断言不可见: {e}")
            return False

    @pytest.mark.run(order=19)
    @pytest.mark.parametrize('project_data', param_data)
    def test_acceptance_confirmation_3(self, project_data):
        """
        测试人员现场验收确认功能
        """
        try:
            self._navigate_to_acceptance_confirmation_3()
            self._submit_acceptance_conclusion_3()
            if self._assert_acceptance_conclusion_3(project_data):
                logger.info('第三次现场验收确认提交成功')
        except Exception as e:
            logger.error(f"第三次现场验收确认提交失败: {e}")
            raise

    def _navigate_to_acceptance_confirmation_3(self):
        """导航到现场验收结论确认页面"""
        self.test_acceptance_confirmation.goto_site_acceptance()
        self.test_acceptance_confirmation.click_enter_acceptance()
        self.test_acceptance_confirmation.click_site_acceptance()

    def _submit_acceptance_conclusion_3(self):
        """提交现场验收结论"""
        self.test_acceptance_confirmation.submit()

    def _assert_acceptance_conclusion_3(self, project_data):
        try:
            self.test_acceptance_confirmation._ele_to_be_expect(project_data['expected'])
            return True
        except Exception as e:
            logger.error(f"断言不可见: {e}")
            return False


if __name__ == '__main__':
    pytest.main(['-v', __file__])
