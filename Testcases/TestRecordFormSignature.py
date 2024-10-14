"""
-*- coding: utf-8 -*-
@File    : TestRecordFormSignature.py
@Date    : 2024/10/11 10:13
@Author  : ggn
"""
import time

import pytest
from BasePage.logger import Logger
from Pages.RecordFormSignature_Page import RecordFormSignaturePage
from Testcases.TestLogin import TestLogin
from Utils.Utils_yaml import load_yaml

logger = Logger("TestRecordFormSignature").get_log()


class TestAcceptanceConfirmation(object):
    yaml_data = load_yaml(r'C:\case\playwright-YTxf\TestDatas\PassingData\Login.yaml')
    if yaml_data is None:
        raise ValueError("无法加载 TestSiteAcceptance.yaml 文件或文件内容为空。")
    login_data = yaml_data[0]

    param_data = load_yaml(r'C:\case\playwright-YTxf\TestDatas\PassingData\TestRecordFormSignature.yaml')
    if param_data is None:
        raise ValueError("无法加载 TestSiteAcceptance.yaml 文件或文件内容为空。")

    @pytest.fixture(autouse=True)
    def set_up(self, page):
        """在每个测试用例前执行"""
        self.login = TestLogin()
        self.login.test_login(page, self.login_data)
        self.test_RecordFormSignature = RecordFormSignaturePage(page)

    @pytest.mark.run(order=6)
    @pytest.mark.parametrize('project_data', param_data)
    def test_acceptance_confirmation(self, project_data):
        """
        测试评定记录表签字
        """
        try:
            self._navigate_to_record_form_signature()
            self._record_form_signature()
            time.sleep(2)
            self._submit_record_form_signature()
            if self._assert_record_form_signature(project_data):
                logger.info('评定记录表签字提交成功')
        except Exception as e:
            logger.error(f"评定记录表签字提交失败: {e}")
            raise

    def _navigate_to_record_form_signature(self):
        self.test_RecordFormSignature.goto_record_form_signature()
        self.test_RecordFormSignature.click_enter_acceptance()
        self.test_RecordFormSignature.click_record_form_signature()

    def _record_form_signature(self):
        self.test_RecordFormSignature.click_signature_button()

    def _submit_record_form_signature(self):
        self.test_RecordFormSignature.submit()

    def _assert_record_form_signature(self, project_data):
        try:
            self.test_RecordFormSignature._ele_to_be_expect(project_data['expected'])
            return True
        except Exception as e:
            logger.error(f"断言不可见: {e}")
            return False

    @pytest.mark.run(order=20)
    @pytest.mark.parametrize('project_data', param_data)
    def test_acceptance_confirmation_2(self, project_data):
        """
        测试评定记录表签字
        """
        try:
            self._navigate_to_record_form_signature_2()
            self._record_form_signature_2()
            time.sleep(2)
            self._submit_record_form_signature_2()
            if self._assert_record_form_signature_2(project_data):
                logger.info('评定记录表签字提交成功')
        except Exception as e:
            logger.error(f"评定记录表签字提交失败: {e}")
            raise

    def _navigate_to_record_form_signature_2(self):
        self.test_RecordFormSignature.goto_record_form_signature()
        self.test_RecordFormSignature.click_enter_acceptance()
        self.test_RecordFormSignature.click_record_form_signature()

    def _record_form_signature_2(self):
        self.test_RecordFormSignature.click_signature_button()

    def _submit_record_form_signature_2(self):
        self.test_RecordFormSignature.submit()

    def _assert_record_form_signature_2(self, project_data):
        try:
            self.test_RecordFormSignature._ele_to_be_expect(project_data['expected'])
            return True
        except Exception as e:
            logger.error(f"断言不可见: {e}")
            return False


if __name__ == '__main__':
    pytest.main(['-s', __file__])
