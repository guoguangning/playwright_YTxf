"""
-*- coding: utf-8 -*-
@File    : TestSignature.py
@Date    : 2024/10/12 16:33
@Author  : ggn
"""
import time

import pytest
from BasePage.logger import Logger
from Pages.Signature_Page import SignaturePage
from Testcases.TestLogin import TestLogin
from Utils.Utils_yaml import load_yaml

logger = Logger("TestSignature").get_log()


class TestAcceptanceConfirmation(object):
    yaml_data = load_yaml(r'C:\case\playwright-YTxf\TestDatas\PassingData\Login.yaml')
    if yaml_data is None:
        raise ValueError("无法加载 TestSiteAcceptance.yaml 文件或文件内容为空。")
    login_data = yaml_data[2]

    param_data = load_yaml(r'C:\case\playwright-YTxf\TestDatas\PassingData\TestSignature.yaml')
    if param_data is None:
        raise ValueError("无法加载 TestSiteAcceptance.yaml 文件或文件内容为空。")

    @pytest.fixture(autouse=True)
    def set_up(self, page):
        """在每个测试用例前执行"""
        self.login = TestLogin()
        self.login.test_login(page, self.login_data)
        self.test_Signature = SignaturePage(page)

    @pytest.mark.run(order=21)
    @pytest.mark.parametrize('project_data', param_data)
    def test_signature(self, project_data):
        """
        测试签字签章功能
        """
        try:
            self._navigate_to_signature()
            self._record_form_signature()
            time.sleep(2)
            self._submit_signature()
            if self._assert_signature(project_data):
                logger.info('签字签章提交成功')
        except Exception as e:
            logger.error(f"签字签章提交失败: {e}")
            raise

    def _navigate_to_signature(self):
        self.test_Signature.goto_signature()
        self.test_Signature.click_enter_acceptance()
        self.test_Signature.click_signature()

    def _record_form_signature(self):
        self.test_Signature.click_signature2()

    def _submit_signature(self):
        self.test_Signature.click_submit_button()

    def _assert_signature(self, project_data):
        try:
            self.test_Signature._ele_to_be_expect(project_data['expected'], project_data['expected_test'])
            return True
        except Exception as e:
            logger.error(f"断言不可见: {e}")
            return False


if __name__ == '__main__':
    pytest.main(['-s', __file__])
