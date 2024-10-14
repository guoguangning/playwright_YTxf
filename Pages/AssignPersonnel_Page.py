"""
-*- coding: utf-8 -*-
@File    : AssignPersonnel_Page.py
@Date    : 2024/10/8 9:21
@Author  : ggn
"""

from BasePage.BasePage import BasePage
from BasePage.logger import Logger
from Utils.Utils_yaml import load_yaml

logger = Logger("AssignPersonnel_Page").get_log()


class AssignPersonnelPage(BasePage):
    AssignPersonnelPage_data = load_yaml(r'C:\case\playwright-YTxf\TestDatas\EleData\AssignPersonnel_Page.yaml')

    def goto_assign_personnel(self):
        try:
            self._goto_url(self.AssignPersonnelPage_data['__path'])
            logger.info("Navigating to Assign_personnel page")
        except Exception as e:
            logger.error(f"Failed to open Assign_personnel page: {e}")
            raise

    def click_enter_acceptance(self) -> None:
        try:
            self._click(self.AssignPersonnelPage_data['__Enter_acceptance'])
            logger.info("Clicking 进入验收")
        except Exception as e:
            logger.error(f"Failed to click 进入验收: {e}")
            raise

    def click_assign_personnel(self) -> None:
        try:
            self._hover(self.AssignPersonnelPage_data['__Assign_personnel'])
            self._click(self.AssignPersonnelPage_data['__Assign_personnel'])
            logger.info("Clicking 分配人员")
        except Exception as e:
            logger.error(f"Failed to click 分配人员: {e}")
            raise

    def click_architecture_no(self) -> None:
        try:
            self._click(self.AssignPersonnelPage_data['__Architecture_no'])
            logger.info("Clicking 建筑专业-无")
        except Exception as e:
            logger.error(f"Failed to click 建筑专业-无: {e}")
            raise

    def select_architecture(self) -> None:
        try:
            self._fill_select(self.AssignPersonnelPage_data['__Architecture'],
                              self.AssignPersonnelPage_data['__Architecture_2'])
            logger.info("Selector 建筑专业")
        except Exception as e:
            logger.error(f"Failed to Selector 建筑专业：{e}")
            raise

    def click_drainage_professional_no(self) -> None:
        try:
            self._click(self.AssignPersonnelPage_data['__Drainage_professional_no'])
            logger.info("Clicking 给排水专业-无")
        except Exception as e:
            logger.error(f"Failed to click 给排水专业-无: {e}")
            raise

    def select_drainage_professional(self) -> None:
        try:
            self._fill_select(self.AssignPersonnelPage_data['__Drainage_professional'],
                              self.AssignPersonnelPage_data['__Drainage_professional_2'])
            logger.info("Selector 给排水专业")
        except Exception as e:
            logger.error(f"Failed to Selector 给排水专业：{e}")
            raise

    def click_electrical_engineering_no(self) -> None:
        try:
            self._click(self.AssignPersonnelPage_data['__Electrical_Engineering_no'])
            logger.info("Clicking 电气专业-无")
        except Exception as e:
            logger.error(f"Failed to click 电气专业-无: {e}")
            raise

    def select_electrical_engineering(self) -> None:
        try:
            self._fill_select(self.AssignPersonnelPage_data['__Electrical_Engineering'],
                              self.AssignPersonnelPage_data['__Electrical_Engineering_2'])
            logger.info("Selector 电气专业")
        except Exception as e:
            logger.error(f"Failed to Selector 电气专业：{e}")
            raise

    def click_hvac_professional_no(self) -> None:
        try:
            self._click(self.AssignPersonnelPage_data['__HVAC_professional_no'])
            logger.info("Clicking 暖通专业-无")
        except Exception as e:
            logger.error(f"Failed to click 暖通专业-无: {e}")
            raise

    def select_hvac_professional(self) -> None:
        try:
            self._fill_select(self.AssignPersonnelPage_data['__HVAC_professional'],
                              self.AssignPersonnelPage_data['__HVAC_professional_2'])
            logger.info("Selector 暖通专业")
        except Exception as e:
            logger.error(f"Failed to Selector 暖通专业：{e}")
            raise

    def click_save(self) -> None:
        try:
            self._click(self.AssignPersonnelPage_data['__save'])
            logger.info("Clicking 保存")
        except Exception as e:
            logger.error(f"Failed to click 保存: {e}")
            raise

    def click_close(self) -> None:
        try:
            self._click(self.AssignPersonnelPage_data['__close'])
            logger.info("Clicking 关闭")
        except Exception as e:
            logger.error(f"Failed to click 关闭: {e}")
            raise

    def click_secondary_confirmation(self):
        try:
            # if self._ele_to_be_expect(self.AssignPersonnelPage_data['__expected'], self.AssignPersonnelPage_data['__expected_text']):
            self._click(self.AssignPersonnelPage_data['__Sure'])
            logger.info("Clicking 提示：二次确认按钮")
        except Exception as e:
            logger.error(f"Failed to click 提示：二次确认按钮: {e}")
