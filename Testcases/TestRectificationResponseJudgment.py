"""
-*- coding: utf-8 -*-
@File    : TestRectificationResponseJudgment.py
@Date    : 2024/10/12 10:27
@Author  : ggn
"""
import pytest
from BasePage.logger import Logger
from Pages.RectificationResponseJudgment_Page import RectificationResponseJudgmentPage
from Testcases.TestLogin import TestLogin
from Utils.Utils_yaml import load_yaml

logger = Logger("TestRectificationResponseJudgment").get_log()


class TestRectificationResponseJudgment(object):
    yaml_data = load_yaml(r'C:\case\playwright-YTxf\TestDatas\PassingData\Login.yaml')
    if yaml_data is None:
        raise ValueError("无法加载 TestSiteAcceptance.yaml 文件或文件内容为空。")
    login_data = yaml_data[0]

    param_data = load_yaml(r'C:\case\playwright-YTxf\TestDatas\PassingData\TestRectificationResponseJudgment.yaml')
    if param_data is None:
        raise ValueError("无法加载 TestSiteAcceptance.yaml 文件或文件内容为空。")

    @pytest.fixture(autouse=True)
    def set_up(self, page):
        """在每个测试用例前执行"""
        self.login = TestLogin()
        self.login.test_login(page, self.login_data)
        self.test_RectificationResponseJudgment = RectificationResponseJudgmentPage(page)

    @pytest.mark.run(order=8)
    @pytest.mark.parametrize('project_data', param_data)
    def test_rectification_response(self, project_data):
        """
        测试整改判定1-1功能
        """
        try:
            self._navigate_to_rectification_response_judgment()
            self._select_input_judgment(project_data)
            self._submit_rectification_response_judgment()
            if self._assert_rectification_response_judgment(project_data):
                logger.info('整改判定提交成功')
        except Exception as e:
            logger.error(f"整改判定提交失败: {e}")
            raise

    def _navigate_to_rectification_response_judgment(self):
        self.test_RectificationResponseJudgment.goto_rectification_response_judgment()
        self.test_RectificationResponseJudgment.click_enter_acceptance()
        self.test_RectificationResponseJudgment.click_rectification_response_judgment()

    def _select_input_judgment(self, project_data):
        self.test_RectificationResponseJudgment.input_judgment(project_data['value'], project_data['files'])

    def _submit_rectification_response_judgment(self):
        self.test_RectificationResponseJudgment.submit()

    def _assert_rectification_response_judgment(self, project_data):
        try:
            self.test_RectificationResponseJudgment._ele_to_be_expect(project_data['expected'])
            return True
        except Exception as e:
            logger.error(f"断言不可见: {e}")
            return False

    @pytest.mark.run(order=11)
    @pytest.mark.parametrize('project_data', param_data)
    def test_rectification_response_2(self, project_data):
        """
        测试整改判定1-2功能
        """
        try:
            self._navigate_to_rectification_response_judgment_2()
            self._select_input_judgment_2()
            self._submit_rectification_response_judgment_2()
            if self._assert_rectification_response_judgment_2(project_data):
                logger.info('整改判定提交成功')
        except Exception as e:
            logger.error(f"整改判定提交失败: {e}")
            raise

    def _navigate_to_rectification_response_judgment_2(self):
        self.test_RectificationResponseJudgment.goto_rectification_response_judgment()
        self.test_RectificationResponseJudgment.click_enter_acceptance()
        self.test_RectificationResponseJudgment.click_rectification_response_judgment()

    def _select_input_judgment_2(self):
        self.test_RectificationResponseJudgment.input_judgment_2()

    def _submit_rectification_response_judgment_2(self):
        self.test_RectificationResponseJudgment.submit()

    def _assert_rectification_response_judgment_2(self, project_data):
        try:
            self.test_RectificationResponseJudgment._ele_to_be_expect(project_data['expected'])
            return True
        except Exception as e:
            logger.error(f"断言不可见: {e}")
            return False

    @pytest.mark.run(order=16)
    @pytest.mark.parametrize('project_data', param_data)
    def test_rectification_response_3(self, project_data):
        """
        测试整改判定2-1功能
        """
        try:
            self._navigate_to_rectification_response_judgment_3()
            self._select_input_judgment_3()
            self._submit_rectification_response_judgment_3()
            if self._assert_rectification_response_judgment_3(project_data):
                logger.info('整改判定提交成功')
        except Exception as e:
            logger.error(f"整改判定提交失败: {e}")
            raise

    def _navigate_to_rectification_response_judgment_3(self):
        self.test_RectificationResponseJudgment.goto_rectification_response_judgment()
        self.test_RectificationResponseJudgment.click_enter_acceptance()
        self.test_RectificationResponseJudgment.click_rectification_response_judgment()

    def _select_input_judgment_3(self):
        self.test_RectificationResponseJudgment.input_judgment_3()

    def _submit_rectification_response_judgment_3(self):
        self.test_RectificationResponseJudgment.submit()

    def _assert_rectification_response_judgment_3(self, project_data):
        try:
            self.test_RectificationResponseJudgment._ele_to_be_expect(project_data['expected'])
            return True
        except Exception as e:
            logger.error(f"断言不可见: {e}")
            return False


if __name__ == '__main__':
    pytest.main(['-s', __file__])
