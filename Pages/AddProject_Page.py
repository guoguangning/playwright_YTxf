"""
-*- coding: utf-8 -*-
@File    : AddProject_Page.py
@Date    : 2024/9/24 15:25
@Author  : ggn
"""
from BasePage.BasePage import BasePage
from BasePage.logger import Logger
from Utils.Utils_yaml import load_yaml

logger = Logger("AddProject_Page").get_log()


class AddProjectPage(BasePage):

    AddProjectPage_data = load_yaml(r'C:\case\playwright-ytxf\TestDatas\EleData\AddProject_Page.yaml')

    def goto_add_project(self):
        try:
            self._goto_url(self.AddProjectPage_data['__path'])
            logger.info("Navigating to AddProject page")
        except Exception as e:
            logger.error(f"Failed to open AddProject page: {e}")
            raise

    def click_new_project_selector(self) -> None:
        try:
            self._click(self.AddProjectPage_data['__New_project_selector'])
            logger.info("Clicking 新增项目")
        except Exception as e:
            logger.error(f"Failed to click 新增项目: {e}")
            raise

    def click_fire_inspection(self) -> None:
        try:
            self._click(self.AddProjectPage_data['__Fire_inspection_selector'])
            logger.info("Clicking 消防验收")
        except Exception as e:
            logger.error(f"Failed to click 消防验收: {e}")
            raise

    def fill_project_name(self, value: str) -> None:
        try:
            self._fill(self.AddProjectPage_data['__Project_Name_selector'], value)
            logger.info("Filling in 工程名称")
        except Exception as e:
            logger.error(f"Failed to fill 工程名称: {e}")
            raise

    def select_project_address(self) -> None:
        try:
            self._select_options(self.AddProjectPage_data['__Project_Address_1'], self.AddProjectPage_data['__Project_Address_2'])
            logger.info("Selector 工程地址")
        except Exception as e:
            logger.error(f"Failed to Selector 工程地址：{e}")
            raise

    def select_category(self) -> None:
        try:
            self._fill_select(self.AddProjectPage_data['__category_1'], *self.AddProjectPage_data['__category_2'])
            self._click(self.AddProjectPage_data['__category_1'])
            logger.info("Selector 类别")
        except Exception as e:
            logger.error(f"Failed to Selector 类别：{e}")
            raise

    def fill_building_number(self, value: str) -> None:
        try:
            self._fill(self.AddProjectPage_data['__Building_Number_selector'], value)
            logger.info("Filling in 建筑层数")
        except Exception as e:
            logger.error(f"Failed to fill 建筑层数: {e}")
            raise

    def fill_building_height(self, value: str) -> None:
        try:
            self._fill(self.AddProjectPage_data['__Building_Height_selector'], value)
            logger.info("Filling in 建筑高度")
        except Exception as e:
            logger.error(f"Failed to fill 建筑高度: {e}")
            raise

    def fill_building_area(self, value: str) -> None:
        try:
            self._fill(self.AddProjectPage_data['__Building_Area_selector'], value)
            logger.info("Filling in 建筑面积")
        except Exception as e:
            logger.error(f"Failed to fill 建筑面积: {e}")
            raise

    def fill_total_building_area(self, value: str) -> None:
        try:
            self._fill(self.AddProjectPage_data['__Total_Building_Area_selector'], value)
            logger.info("Filling in 建筑总面积")
        except Exception as e:
            logger.error(f"Failed to fill 建筑总面积: {e}")
            raise

    def fill_building_volume_selector(self, value: str) -> None:
        try:
            self._fill(self.AddProjectPage_data['__Building_volume_selector'], value)
            logger.info("Filling in 建筑体积")
        except Exception as e:
            logger.error(f"Failed to fill 建筑体积: {e}")
            raise

    def select_use_nature(self) -> None:
        try:
            self._select_options(self.AddProjectPage_data['__Use_nature_1'], self.AddProjectPage_data['__Use_nature_2'])
            logger.info("Selector 使用性质")
        except Exception as e:
            logger.error(f"Failed to Selector 使用性质：{e}")
            raise

    def fill_description_of_usage(self, value: str) -> None:
        try:
            self._fill(self.AddProjectPage_data['__Description_of_usage'], value)
            logger.info("Filling in 使用性质说明")
        except Exception as e:
            logger.error(f"Failed to fill 使用性质说明: {e}")
            raise

    def fill_building_construction_selector(self, value: str) -> None:
        try:
            self._fill(self.AddProjectPage_data['__Building_Construction_selector'], value)
            logger.info("Filling in 建筑结构")
        except Exception as e:
            logger.error(f"Failed to fill 建筑结构: {e}")
            raise

    def fill_fire_level(self, value: str) -> None:
        try:
            self._fill(self.AddProjectPage_data['__Fire_level_selector'], value)
            logger.info("Filling in 耐火等级")
        except Exception as e:
            logger.error(f"Failed to fill 耐火等级: {e}")
            raise

    def fill_hazard_classification(self, value: str) -> None:
        try:
            self._fill(self.AddProjectPage_data['__Hazard_Classification_selector'], value)
            logger.info("Filling in 建筑/火灾危险性分类")
        except Exception as e:
            logger.error(f"Failed to fill 建筑/火灾危险性分类: {e}")
            raise

    def click_filing_date_selector(self) -> None:
        try:
            self._select_date(self.AddProjectPage_data['__Filing_date_selector'])
            logger.info("Clicking 建设单位申请消防备案时间")
        except Exception as e:
            logger.error(f"Failed to selector 建设单位申请消防备案时间：{e}")
            raise

    def select_construction_unit(self, value: str) -> None:
        try:
            self._fill_select(self.AddProjectPage_data['__Construction_Unit_1'], self.AddProjectPage_data['__Construction_Unit_2'], input_value=value)
            logger.info("建设单位")
        except Exception as e:
            logger.error(f"Failed to Selector 建设单位：{e}")
            raise

    def select_technical_leader(self) -> None:
        try:
            self._fill_select(self.AddProjectPage_data['__Technical_leader_1'], self.AddProjectPage_data['__Technical_leader_2'])
            logger.info("Selector 技术负责人")
        except Exception as e:
            logger.error(f"Failed to Selector 技术负责人：{e}")
            raise

    def click_temporarily_save_button(self) -> None:
        try:
            self._click(self.AddProjectPage_data['__Temporarily_save_button_selector'])
            logger.info("Clicking 暂存按钮")
        except Exception as e:
            logger.error(f"Failed to click 暂存按钮: {e}")
            raise

    def click_submit_button(self) -> None:
        try:
            self._click(self.AddProjectPage_data['__Submit_button_selector'])
            logger.info("Clicking 提交按钮")
        except Exception as e:
            logger.error(f"Failed to click 提交按钮: {e}")
            raise
