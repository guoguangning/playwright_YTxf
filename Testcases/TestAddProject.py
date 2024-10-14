"""
-*- coding: utf-8 -*-
@File    : TestAddProject.py
@Date    : 2024/9/24 15:25
@Author  : ggn
"""

import pytest
from Pages.AddProject_Page import AddProjectPage
from BasePage.logger import Logger
from Testcases.TestLogin import TestLogin
from Utils.Utils_yaml import load_yaml

logger = Logger("TestAddProject").get_log()


class TestAddProject(object):
    yaml_data = load_yaml(r'C:\case\playwright-YTxf\TestDatas\PassingData\Login.yaml')
    if yaml_data is None:
        raise ValueError("无法加载 TestSiteAcceptance.yaml 文件或文件内容为空。")
    login_data = yaml_data[0]

    param_data = load_yaml(r'C:\case\playwright-YTxf\TestDatas\PassingData\TestAddProject.yaml')
    if param_data is None:
        raise ValueError("无法加载 TestSiteAcceptance.yaml 文件或文件内容为空。")

    @pytest.fixture(autouse=True)
    def set_up(self, page):
        """在每个测试用例前执行"""
        self.login = TestLogin()
        self.login.test_login(page, self.login_data)
        self.test_add_project = AddProjectPage(page)  # 创建 AddProject 实例

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('project_data', param_data)
    def test_add_project_full(self, project_data):
        """
        测试新建消防查验项目
        """
        try:
            # 新增消防查验
            self._add_fire_inspection_project(project_data)
            # 提交并确认
            self._submit_project()
            # 处理单位未注册情况
            self._handle_unit_not_registered()
            # 断言
            self._assert_project_added(project_data)
        except Exception as e:
            logger.error(f"添加消防查验项目失败: {e}")
            raise

    def _add_fire_inspection_project(self, project_data):
        self.test_add_project.goto_add_project()
        self.test_add_project.click_new_project_selector()
        self.test_add_project.click_fire_inspection()
        self.test_add_project.fill_project_name(project_data['project_name'])
        self.test_add_project.select_project_address()
        self.test_add_project.select_category()
        self.test_add_project.fill_building_number(project_data['building_number'])
        self.test_add_project.fill_building_height(project_data['building_height'])
        self.test_add_project.fill_building_area(project_data['building_area'])
        self.test_add_project.fill_total_building_area(project_data['total_building_area'])
        self.test_add_project.select_use_nature()
        self.test_add_project.fill_fire_level(project_data['fire_level'])
        self.test_add_project.select_technical_leader()

        if project_data['building_volume']:
            self.test_add_project.fill_building_volume_selector(project_data['building_volume'])
            self.test_add_project.fill_description_of_usage(project_data['description_of_usage'])
            self.test_add_project.fill_building_construction_selector(project_data['building_construction'])
            self.test_add_project.fill_hazard_classification(project_data['hazard_classification'])
            self.test_add_project.select_construction_unit(project_data['construction_unit'])
            self.test_add_project.click_filing_date_selector()

    def _submit_project(self):
        self.test_add_project.click_submit_button()
        self.test_add_project.click_submit_two_button()

    def _handle_unit_not_registered(self):
        self.test_add_project.click_unit_not_registered_button()
        # self.test_add_project.select_construction_unit(project_data['construction_unit'])
        # self._submit_project()

    def _assert_project_added(self, project_data):
        try:
            self.test_add_project._ele_to_be_expect(project_data['expected'])
        except Exception as e:
            logger.error(f"断言不可见: {e}")
            raise


if __name__ == '__main__':
    pytest.main(['-v', __file__])
