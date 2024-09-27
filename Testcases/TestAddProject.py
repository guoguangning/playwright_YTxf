# TestAddProject.py
import pytest
from playwright.sync_api import sync_playwright
from Pages.AddProject_Page import AddProjectPage
from BasePage.logger import Logger
from Testcases.TestLogin import TestLogin

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

    @pytest.fixture(autouse=True)
    def set_up(self, page):
        """在每个测试用例前执行登录"""
        self.login = TestLogin()
        self.login.test_login(page, '13723945525', 'Th#VHv1P6T3s53Ug', '//*[@id="app"]/div[1]/div[1]/img')
        self.test_add_project = AddProjectPage(page)  # 创建 AddProject 实例

    project_data = [
        ('验收工程名称', '建筑层数', '建筑高度', '建筑面积', '110', '耐火等级',
         '//tbody/tr/td[3]/div[text()="验收工程名称"]', '建筑体积', '使用性质说明', '建筑结构',
         '建筑/火灾危险性分类', '滨州建设单位3210',),
        ('验收工程名称2', '建筑层数', '建筑高度', '建筑面积', '110', '耐火等级',
         '//tbody/tr/td[3]/div[text()="验收工程名称2"]', '', '', '', '', '')
    ]

    @pytest.mark.parametrize(
        'project_name, building_number, building_height, building_area, total_building_area, fire_level, expected,'
        ' building_volume, description_of_usage, building_construction, hazard_classification, construction_unit, ',
        project_data)
    def test_add_project_full(self, page, project_name, building_number, building_height, building_area,
                              total_building_area, fire_level, expected,
                              building_volume, description_of_usage, building_construction,
                              hazard_classification, construction_unit):
        """
        测试新建消防查验项目全量参数
        :param page:
        :param project_name: 工程名称
        :param building_number:建筑层数
        :param building_height:建筑高度
        :param building_area:建筑面积
        :param total_building_area:建筑总面积
        :param building_volume:建筑体积 非必填
        :param description_of_usage:使用性质说明 非必填
        :param building_construction:建筑结构  非必填
        :param fire_level:耐火等级
        :param hazard_classification:建筑/火灾危险性分类 非必填
        :param construction_unit:建设单位 非必填
        :param expected: 断言元素
        """

        try:
            # 新增消防查验
            self.test_add_project.goto_add_project()
            self.test_add_project.click_new_project_selector()
            self.test_add_project.click_fire_inspection()
            self.test_add_project.fill_project_name(project_name)
            self.test_add_project.select_project_address()
            self.test_add_project.select_category()
            self.test_add_project.fill_building_number(building_number)
            self.test_add_project.fill_building_height(building_height)
            self.test_add_project.fill_building_area(building_area)
            self.test_add_project.fill_total_building_area(total_building_area)
            self.test_add_project.select_use_nature()
            self.test_add_project.fill_fire_level(fire_level)
            self.test_add_project.select_technical_leader()

            if building_volume:
                self.test_add_project.fill_building_volume_selector(building_volume)
                self.test_add_project.fill_description_of_usage(description_of_usage)
                self.test_add_project.fill_building_construction_selector(building_construction)
                self.test_add_project.fill_hazard_classification(hazard_classification)
                self.test_add_project.click_filing_date_selector()
                self.test_add_project.select_construction_unit(construction_unit)

            # 暂存
            self.test_add_project.click_temporarily_save_button()

            try:
                self.test_add_project._ele_to_be_visible(expected)
                logger.info("断言可见")
            except Exception as e:
                logger.error(f"断言不可见: {e}")
                raise
            # 提交
            # self.test_add_project.click_submit_button()

        except Exception as e:
            logger.error(f"添加消防查验项目失败: {e}")
            raise


if __name__ == '__main__':
    pytest.main(['-v', __file__])
