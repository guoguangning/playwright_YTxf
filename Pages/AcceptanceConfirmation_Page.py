"""
-*- coding: utf-8 -*-
@File    : AcceptanceConfirmation_Page.py
@Date    : 2024/10/10 16:31
@Author  : ggn
"""
from BasePage.BasePage import BasePage
from BasePage.logger import Logger
from Utils.Utils_yaml import load_yaml

logger = Logger("AcceptanceConfirmation_Page").get_log()


class AcceptanceConfirmationPage(BasePage):
    AcceptanceConfirmation_data = load_yaml(r'C:\case\playwright-YTxf\TestDatas\EleData\AcceptanceConfirmation_Page.yaml')

    def goto_site_acceptance(self):
        try:
            self._goto_url(self.AcceptanceConfirmation_data['__path'])
            logger.info("Navigating to SiteAcceptance page")
        except Exception as e:
            logger.error(f"Failed to open SiteAcceptance page: {e}")
            raise

    def click_enter_acceptance(self) -> None:
        try:
            self._click(self.AcceptanceConfirmation_data['__Enter_acceptance'])
            logger.info("Click 进入验收")
        except Exception as e:
            logger.error(f"Failed to click 进入验收失败: {e}")
            raise

    def click_site_acceptance(self) -> None:
        try:
            self._click(self.AcceptanceConfirmation_data['__site_acceptance'])
            logger.info("Click 现场验收")
        except Exception as e:
            logger.error(f"Failed to Click 现场验收失败: {e}")
            raise

    def submit(self) -> None:
        try:
            self._click(self.AcceptanceConfirmation_data['__Submit_button'])
            self._click(self.AcceptanceConfirmation_data['__Double_confirmation_button'])
            logger.info("Submit 验收结论完毕 ")
        except Exception as e:
            logger.error(f"Failed to Submit 验收结论失败: {e}")
            raise
