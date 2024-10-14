"""
-*- coding: utf-8 -*-
@File    : Signature_Page.py
@Date    : 2024/10/12 16:25
@Author  : ggn
"""
from BasePage.BasePage import BasePage
from BasePage.logger import Logger
from Utils.Utils_yaml import load_yaml

logger = Logger("Signature_Page").get_log()


class SignaturePage(BasePage):
    SiteAcceptancePage_data = load_yaml(r'C:\case\playwright-YTxf\TestDatas\EleData\Signature_Page.yaml')

    def goto_signature(self):
        try:
            self._goto_url(self.SiteAcceptancePage_data['__path'])
            logger.info("Navigating to SiteAcceptance page")
        except Exception as e:
            logger.error(f"Failed to open SiteAcceptance page: {e}")
            raise

    def click_enter_acceptance(self) -> None:
        try:
            self._click(self.SiteAcceptancePage_data['__Enter_acceptance'])
            logger.info("Click 进入验收")
        except Exception as e:
            logger.error(f"Failed to click 进入验收失败: {e}")
            raise

    def click_signature(self) -> None:
        try:
            self._click(self.SiteAcceptancePage_data['__site_acceptance'])
            logger.info("Click 签章")
        except Exception as e:
            logger.error(f"Failed to Click 签章失败: {e}")
            raise

    def click_signature2(self) -> None:
        try:
            self._click(self.SiteAcceptancePage_data['__Signature'])
            self._click(self.SiteAcceptancePage_data['__Signature_confirmation_button'])
            logger.info("Click 签章按钮")
        except Exception as e:
            logger.error(f"Failed to Click 签章按钮失败: {e}")
            raise

    def click_submit_button(self) -> None:
        try:
            self._click(self.SiteAcceptancePage_data['__Submit_button'])
            self._click(self.SiteAcceptancePage_data['__Submit_confirmation_button'])
            logger.info("Click 提交按钮")
        except Exception as e:
            logger.error(f"Failed to Click 提交按钮失败: {e}")
            raise
