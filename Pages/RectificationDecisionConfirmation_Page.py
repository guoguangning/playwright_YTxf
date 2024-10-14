"""
-*- coding: utf-8 -*-
@File    : RectificationDecisionConfirmation_Page.py
@Date    : 2024/10/12 10:54
@Author  : ggn
"""
from BasePage.BasePage import BasePage
from BasePage.logger import Logger
from Utils.Utils_yaml import load_yaml

logger = Logger("RectificationDecisionConfirmation_Page").get_log()


class RectificationDecisionConfirmationPage(BasePage):
    RectificationDecisionConfirmation_data = load_yaml(
        r'C:\case\playwright-YTxf\TestDatas\EleData\RectificationDecisionConfirmation_Page.yaml')

    def goto_rectification_decision_confirmation(self):
        try:
            self._goto_url(self.RectificationDecisionConfirmation_data['__path'])
            logger.info("Navigating to RectificationDecisionConfirmation page")
        except Exception as e:
            logger.error(f"Failed to open RectificationDecisionConfirmation page: {e}")
            raise

    def click_enter_acceptance(self) -> None:
        try:
            self._click(self.RectificationDecisionConfirmation_data['__Enter_acceptance'])
            logger.info("Click 进入验收")
        except Exception as e:
            logger.error(f"Failed to click 进入验收失败: {e}")
            raise

    def click_rectification_decision_confirmation(self) -> None:
        try:
            self._click(self.RectificationDecisionConfirmation_data['__RectificationDecisionConfirmation'])
            logger.info("Click 现场验收")
        except Exception as e:
            logger.error(f"Failed to Click 现场验收失败: {e}")
            raise

    def submit(self) -> None:
        try:
            self._click(self.RectificationDecisionConfirmation_data['__Submit_button'])
            self._click(self.RectificationDecisionConfirmation_data['__Double_confirmation_button'])
            logger.info("Submit 整改判定确认完毕 ")
        except Exception as e:
            logger.error(f"Failed to Submit 整改判定确认失败: {e}")
            raise
