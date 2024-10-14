"""
-*- coding: utf-8 -*-
@File    : RectificationResponse_Page.py
@Date    : 2024/10/11 14:58
@Author  : ggn
"""
from BasePage.BasePage import BasePage
from BasePage.logger import Logger
from Utils.Utils_yaml import load_yaml

logger = Logger("RectificationResponse_Page").get_log()


class RectificationResponsePage(BasePage):
    RectificationResponse_data = load_yaml(r'C:\case\playwright-YTxf\TestDatas\EleData\RectificationResponse_Page.yaml')

    def goto_rectification_response(self):
        try:
            self._goto_url(self.RectificationResponse_data['__path'])
            logger.info("Navigating to RectificationResponse page")
        except Exception as e:
            logger.error(f"Failed to open RectificationResponse page: {e}")
            raise

    def click_enter_acceptance(self) -> None:
        try:
            self._click(self.RectificationResponse_data['__Enter_acceptance'])
            logger.info("Click 进入验收")
        except Exception as e:
            logger.error(f"Failed to click 进入验收失败: {e}")
            raise

    def click_rectification_response(self) -> None:
        try:
            self._click(self.RectificationResponse_data['__Record_RectificationResponse'])
            logger.info("Click 整改回复")
        except Exception as e:
            logger.error(f"Failed to click 整改回复失败: {e}")
            raise

    def input_reply(self, value, files) -> None:
        try:
            self._fill(self.RectificationResponse_data['__Response'], value)
            self._click(self.RectificationResponse_data['__Response_Images'])
            self._file(self.RectificationResponse_data['__Response_Images_input'], files)
            self._click(self.RectificationResponse_data['__Response_Images_save'])

            self._fill(self.RectificationResponse_data['__Response2'], value)
            logger.info("Input 1-1回复")
        except Exception as e:
            logger.error(f"Failed to Input 1-1回复失败: {e}")
            raise

    def input_reply_2(self, value) -> None:
        try:
            self._fill(self.RectificationResponse_data['__Response3'], value)
            logger.info("Input 1-2回复")
        except Exception as e:
            logger.error(f"Failed to Input 1-2回复失败: {e}")
            raise

    def input_reply_3(self, value, value2) -> None:
        try:
            self._fill(self.RectificationResponse_data['__Response4'], value)
            self._fill(self.RectificationResponse_data['__Response5'], value2)
            logger.info("Input 2-1回复")
        except Exception as e:
            logger.error(f"Failed to Input 2-1回复失败: {e}")
            raise

    def submit(self) -> None:
        try:
            self._click(self.RectificationResponse_data['__Submit_button'])
            self._click(self.RectificationResponse_data['__Double_confirmation_button'])
            logger.info("Submit 1-1回复 ")
        except Exception as e:
            logger.error(f"Failed to Submit 1-1回复失败: {e}")
            raise
