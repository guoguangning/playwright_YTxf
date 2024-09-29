"""
-*- coding: utf-8 -*-
@File    : TestAddProject.py
@Date    : 2024/9/24 15:25
@Author  : ggn
"""

import pytest
from playwright.sync_api import sync_playwright
from Pages.AddProject_Page import AddProjectPage
from BasePage.logger import Logger
from Testcases.TestLogin import TestLogin
from Utils.Utils_yaml import load_yaml

logger = Logger("TestAddProject").get_log()


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=['--start-maximized'])
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    yield page
    context.close()


class TestAddProject(object):
    login_data = load_yaml(r'C:\case\playwright-ytxf\TestDatas\PassingData\TestLogin.yaml')[0]

    @pytest.fixture(autouse=True)
    def set_up(self, page):
        """在每个测试用例前执行"""
        self.login = TestLogin()
        self.login.test_login(page, self.login_data)
        self.test_add_project = AddProjectPage(page)  # 创建 AddProject 实例

    @pytest.mark.parametrize('project_data',
                             load_yaml(r'C:\case\playwright-ytxf\TestDatas\PassingData\TestAddProject.yaml'))
    def test_add_project_full(self, project_data):
        """
        测试新建消防查验项目
        """
        try:
            # 新增消防查验
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
                self.test_add_project.click_filing_date_selector()
                self.test_add_project.select_construction_unit(project_data['construction_unit'])

            # 暂存
            self.test_add_project.click_temporarily_save_button()
            # 提交
            # self.test_add_project.click_submit_button()

            try:
                self.test_add_project._ele_to_be_visible(project_data['expected'])
                logger.info("断言可见")
            except Exception as e:
                logger.error(f"断言不可见: {e}")
                raise

        except Exception as e:
            logger.error(f"添加消防查验项目失败: {e}")
            raise


if __name__ == '__main__':
    pytest.main(['-v', __file__])
