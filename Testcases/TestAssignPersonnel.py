"""
-*- coding: utf-8 -*-
@File    : TestAssignPersonnel.py
@Date    : 2024/10/8 16:24
@Author  : ggn
"""
import pytest
from BasePage.logger import Logger
from Pages.AssignPersonnel_Page import AssignPersonnelPage
from Testcases.TestLogin import TestLogin
from Utils.Utils_yaml import load_yaml

logger = Logger("TestAssignPersonnel").get_log()


class TestAssignPersonnel:
    yaml_data = load_yaml(r'C:\case\playwright-YTxf\TestDatas\PassingData\Login.yaml')
    if yaml_data is None:
        raise ValueError("无法加载 TestSiteAcceptance.yaml 文件或文件内容为空。")
    login_data = yaml_data[0]

    param_data = load_yaml(r'C:\case\playwright-YTxf\TestDatas\PassingData\TestAssignPersonnel.yaml')
    if param_data is None:
        raise ValueError("无法加载 TestSiteAcceptance.yaml 文件或文件内容为空。")

    @pytest.fixture(autouse=True)
    def set_up(self, page):
        """在每个测试用例前执行"""
        self.login = TestLogin()
        self.login.test_login(page, self.login_data)
        self.test_assign_personnel = AssignPersonnelPage(page)

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('project_data', param_data)
    def test_assign_personnel(self, project_data):
        """
        测试人员分配功能
        """
        try:
            self._navigate_to_assign_personnel()
            self._select_professionals(project_data)
            self._save_assignment()
            if self._assert_assign_personnel(project_data):
                logger.info('分配人员成功')
        except Exception as e:
            logger.error(f"分配人员失败: {e}")
            raise

    def _navigate_to_assign_personnel(self):
        """导航到分配人员页面"""
        self.test_assign_personnel.goto_assign_personnel()
        self.test_assign_personnel.click_enter_acceptance()
        self.test_assign_personnel.click_assign_personnel()

    def _select_professionals(self, project_data):
        """根据提供的项目数据选择专业人员"""
        self.test_assign_personnel.select_architecture()

        if project_data['Drainage_professional']:
            self.test_assign_personnel.select_drainage_professional()
            self.test_assign_personnel.select_electrical_engineering()
            self.test_assign_personnel.select_hvac_professional()
        else:
            self.test_assign_personnel.click_drainage_professional_no()
            self.test_assign_personnel.click_electrical_engineering_no()
            self.test_assign_personnel.click_hvac_professional_no()

    def _save_assignment(self):
        """保存分配并进行二次确认"""
        self.test_assign_personnel.click_save()
        self.test_assign_personnel.click_secondary_confirmation()

    def _assert_assign_personnel(self, project_data):
        try:
            self.test_assign_personnel._ele_to_be_expect(project_data['expected'])
            return True
        except Exception as e:
            logger.error(f"断言不可见: {e}")
            return False


if __name__ == '__main__':
    pytest.main(['-v', __file__])
