"""
-*- coding: utf-8 -*-
@File    : RectificationResponseJudgment_Page.py
@Date    : 2024/10/12 10:20
@Author  : ggn
"""

from BasePage.BasePage import BasePage
from BasePage.logger import Logger
from Utils.Utils_yaml import load_yaml

logger = Logger("RectificationResponseJudgment_Page").get_log()


class RectificationResponseJudgmentPage(BasePage):
    RectificationResponseJudgment_data = load_yaml(r'C:\case\playwright-YTxf\TestDatas\EleData\RectificationResponseJudgment_Page.yaml')

    def goto_rectification_response_judgment(self):
        try:
            self._goto_url(self.RectificationResponseJudgment_data['__path'])
            logger.info("Navigating to RectificationResponseJudgment page")
        except Exception as e:
            logger.error(f"Failed to open RectificationResponseJudgment page: {e}")
            raise

    def click_enter_acceptance(self) -> None:
        try:
            self._click(self.RectificationResponseJudgment_data['__Enter_acceptance'])
            logger.info("Click 进入验收")
        except Exception as e:
            logger.error(f"Failed to click 进入验收失败: {e}")
            raise

    def click_rectification_response_judgment(self) -> None:
        try:
            self._click(self.RectificationResponseJudgment_data['__RectificationResponseJudgment'])
            logger.info("Click 现场验收")
        except Exception as e:
            logger.error(f"Failed to click 现场验收失败: {e}")
            raise

    def input_judgment(self, value, files) -> None:
        try:
            self._click(self.RectificationResponseJudgment_data['__Reply_judgment'])
            self._fill(self.RectificationResponseJudgment_data['__Disagree_reply'], value)
            self._click(self.RectificationResponseJudgment_data['__Disagree_reply_images'])
            self._file(self.RectificationResponseJudgment_data['__Disagree_reply_images_input'], files)
            self._click(self.RectificationResponseJudgment_data['__Disagree_reply_images_save'])

            self._click(self.RectificationResponseJudgment_data['__Reply_judgment2'])
            logger.info("Input 整改判定1-1")
        except Exception as e:
            logger.error(f"Failed to Input 整改判定1-1: {e}")
            raise

    def input_judgment_2(self) -> None:
        try:
            self._click(self.RectificationResponseJudgment_data['__Reply_judgment3'])
            logger.info("Input 整改判定1-2")
        except Exception as e:
            logger.error(f"Failed to Input 整改判定1-2: {e}")
            raise

    def input_judgment_3(self) -> None:
        try:
            self._click(self.RectificationResponseJudgment_data['__Reply_judgment4'])
            self._click(self.RectificationResponseJudgment_data['__Reply_judgment5'])
            logger.info("Input 整改判定2-1")
        except Exception as e:
            logger.error(f"Failed to Input 整改判定2-1: {e}")
            raise

    def submit(self) -> None:
        try:
            self._click(self.RectificationResponseJudgment_data['__Submit_button'])
            self._click(self.RectificationResponseJudgment_data['__Double_confirmation_button'])
            logger.info("Submit 整改判定 ")
        except Exception as e:
            logger.error(f"Failed to Submit 整改判定失败: {e}")
            raise
