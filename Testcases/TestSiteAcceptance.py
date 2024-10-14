"""
-*- coding: utf-8 -*-
@File    : TestSiteAcceptance.py
@Date    : 2024/10/9 15:34
@Author  : ggn
"""
import time

import pytest
from BasePage.logger import Logger
from Pages.SiteAcceptance_Page import SiteAcceptancePage
from Testcases.TestLogin import TestLogin
from Utils.Utils_yaml import load_yaml

logger = Logger("TestSiteAcceptance").get_log()


class TestSiteAcceptance(object):
    yaml_data = load_yaml(r'C:\case\playwright-YTxf\TestDatas\PassingData\Login.yaml')
    if yaml_data is None:
        raise ValueError("无法加载 TestSiteAcceptance.yaml 文件或文件内容为空。")
    login_data = yaml_data[0]

    param_data = load_yaml(r'C:\case\playwright-YTxf\TestDatas\PassingData\TestSiteAcceptance.yaml')
    if param_data is None:
        raise ValueError("无法加载 TestSiteAcceptance.yaml 文件或文件内容为空。")

    @pytest.fixture(autouse=True)
    def set_up(self, page):
        """在每个测试用例前执行"""
        self.login = TestLogin()
        self.login.test_login(page, self.login_data)
        self.test_site_acceptance = SiteAcceptancePage(page)

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('project_data', param_data)
    def test_site_acceptance(self, project_data):
        """
        测试现场验收功能
        """
        try:
            self._navigate_to_site_acceptance()
            self._select_table_conclusion(project_data)
            self._submit_conclusion()
            self._assert_site_acceptance(project_data)
            logger.info('现场验收提交成功')
        except Exception as e:
            logger.error(f"现场验收提交失败: {e}")
            raise

    def _navigate_to_site_acceptance(self):
        """导航到现场验收结论填写页面"""
        self.test_site_acceptance.goto_site_acceptance()
        self.test_site_acceptance.click_enter_acceptance()
        self.test_site_acceptance.click_site_acceptance()

    def _select_table_conclusion(self, project_data):
        """选择表结论"""
        self.test_site_acceptance.select_table_2()
        self.test_site_acceptance.select_table_3()
        self.test_site_acceptance.select_table_4()
        self.test_site_acceptance.select_table_5()
        self.test_site_acceptance.select_table_6()
        self.test_site_acceptance.select_table_7()
        self.test_site_acceptance.select_table_8()
        self.test_site_acceptance.select_table_9()
        self.test_site_acceptance.select_table_10()
        self.test_site_acceptance.select_table_11()
        self.test_site_acceptance.select_table_12()
        self.test_site_acceptance.select_table_13()
        self.test_site_acceptance.select_table_14()
        self.test_site_acceptance.select_table_15()

        if project_data['Question_1']:
            self.test_site_acceptance.select_table_1(project_data['Question_1'], project_data['Question_2'],
                                                     project_data['files'])
        else:
            self.test_site_acceptance.select_table_1_pass()

    def _submit_conclusion(self):
        self.test_site_acceptance.submit()

    def _assert_site_acceptance(self, project_data):
        try:
            self.test_site_acceptance._ele_to_be_expect(project_data['expected'])
            return True
        except Exception as e:
            logger.error(f"断言不可见: {e}")
            return False

    @pytest.mark.run(order=13)
    @pytest.mark.parametrize('project_data', param_data)
    def test_site_acceptance_2(self, project_data):
        """
        测试现场验收功能(第二次)
        """
        try:
            self._navigate_to_site_acceptance_2()
            self._select_table_conclusion_2(project_data)
            time.sleep(2)
            self._submit_conclusion_2()
            if self._assert_site_acceptance_2(project_data):
                logger.info('现场验收提交成功')
        except Exception as e:
            logger.error(f"现场验收提交失败: {e}")
            raise

    def _navigate_to_site_acceptance_2(self):
        """导航到现场验收结论填写页面"""
        self.test_site_acceptance.goto_site_acceptance()
        self.test_site_acceptance.click_enter_acceptance()
        self.test_site_acceptance.click_site_acceptance()

    def _select_table_conclusion_2(self, project_data):
        """选择表结论"""
        self.test_site_acceptance.select_table_1_2(project_data['Question_1-2'], project_data['Question_3'])

    def _submit_conclusion_2(self):
        self.test_site_acceptance.submit()

    def _assert_site_acceptance_2(self, project_data):
        try:
            self.test_site_acceptance._ele_to_be_expect(project_data['expected'])
            return True
        except Exception as e:
            logger.error(f"断言不可见: {e}")
            return False

    @pytest.mark.run(order=18)
    @pytest.mark.parametrize('project_data', param_data)
    def test_site_acceptance_3(self, project_data):
        """
        测试现场验收功能(第三次)
        """
        try:
            self._navigate_to_site_acceptance_3()
            self._select_table_conclusion_3()
            self._submit_conclusion_3()
            if self._assert_site_acceptance_3(project_data):
                logger.info('现场验收提交成功')
        except Exception as e:
            logger.error(f"现场验收提交失败: {e}")
            raise

    def _navigate_to_site_acceptance_3(self):
        """导航到现场验收结论填写页面"""
        self.test_site_acceptance.goto_site_acceptance()
        self.test_site_acceptance.click_enter_acceptance()
        self.test_site_acceptance.click_site_acceptance()

    def _select_table_conclusion_3(self, ):
        """选择表结论"""
        self.test_site_acceptance.select_table_1_3()

    def _submit_conclusion_3(self):
        self.test_site_acceptance.submit()

    def _assert_site_acceptance_3(self, project_data):
        try:
            self.test_site_acceptance._ele_to_be_expect(project_data['expected'])
            return True
        except Exception as e:
            logger.error(f"断言不可见: {e}")
            return False


if __name__ == '__main__':
    pytest.main(['-v', __file__])
