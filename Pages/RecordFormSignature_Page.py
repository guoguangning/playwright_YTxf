"""
-*- coding: utf-8 -*-
@File    : RecordFormSignature_Page.py
@Date    : 2024/10/11 9:59
@Author  : ggn
"""
from BasePage.BasePage import BasePage
from BasePage.logger import Logger
from Utils.Utils_yaml import load_yaml

logger = Logger("RecordFormSignature_Page").get_log()


class RecordFormSignaturePage(BasePage):
    RecordFormSignature_data = load_yaml(r'C:\case\playwright-YTxf\TestDatas\EleData\RecordFormSignature_Page.yaml')

    def goto_record_form_signature(self):
        try:
            self._goto_url(self.RecordFormSignature_data['__path'])
            logger.info("Navigating to RecordFormSignature page")
        except Exception as e:
            logger.error(f"Failed to open RecordFormSignature page: {e}")
            raise

    def click_enter_acceptance(self) -> None:
        try:
            self._click(self.RecordFormSignature_data['__Enter_acceptance'])
            logger.info("Click 进入验收")
        except Exception as e:
            logger.error(f"Failed to click 进入验收失败: {e}")
            raise

    def click_record_form_signature(self) -> None:
        try:
            self._click(self.RecordFormSignature_data['__Record_Form_Signature'])
            logger.info("Click 现场评定记录表签字")
        except Exception as e:
            logger.error(f"Failed to click 现场评定记录表签字失败: {e}")
            raise

    def click_signature_button(self) -> None:
        try:
            self._click(self.RecordFormSignature_data['__Signature_button'])
            if self._ele_to_be_expect(self.RecordFormSignature_data['__Signature_expected'], self.RecordFormSignature_data['__Signature_expected_test']):
                logger.info("Click 记录表签字成功")
        except Exception as e:
            logger.error(f"Failed to click 记录表签字失败: {e}")
            raise

    def submit(self) -> None:
        try:
            self._click(self.RecordFormSignature_data['__Submit_button'])
            self._click(self.RecordFormSignature_data['__Double_confirmation_button'])
            logger.info("Submit 现场评定记录表签字提交成功 ")
        except Exception as e:
            logger.error(f"Failed to Submit 现场评定记录表签字提交失败: {e}")
            raise
