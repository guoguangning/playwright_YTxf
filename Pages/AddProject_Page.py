from BasePage.BasePage import BasePage
from BasePage.logger import Logger

logger = Logger("AddProject_Page").get_log()


class AddProjectPage(BasePage):

    __path = '/myAssignment/myAssignment/myAssignment'

    __New_project_selector = '//div[@class="el-scrollbar theme-light"]/div/div/ul/div[1]'
    __Fire_inspection_selector = '//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/div/ul/div[1]/li/ul/div[2]'

    __Project_Name_selector = '//input[@placeholder="请输入工程名称"]'

    # 工程地址
    __Project_Address_1 = '//form[@class="el-form form el-form--inline"]/div[2]/div[2]'  # 下拉框元素
    __Project_Address_2 = '//div[@x-placement="bottom-start"]/div/div/ul/li/span[text()="市辖区"]'  # 选择元素
    __Project_Address_3 = '市辖区高新区芝罘区福山区牟平区莱山区蓬莱区经济技术开发区龙口市莱阳市莱州市招远市栖霞市海阳市'
    __Project_Address_4 = '招远市'

    # 类别
    __category_1 = '//form[@class="el-form form el-form--inline"]/div[3]/div[2]'
    __category_2 = ['//div[@class="el-select-dropdown el-popper is-multiple"]/div/div/ul/li/span[text()="新建"]',
                    '//div[@class="el-select-dropdown el-popper is-multiple"]/div/div/ul/li/span[text()="建筑保温"]']
    # 使用性质
    __Use_nature_1 = '//form[@class="el-form form el-form--inline"]/div[9]/div[2]'
    __Use_nature_2 = '//div[@x-placement="bottom-start"]/div/div/ul/li/span[text()="民用"]'
    __Use_nature_3 = '工业民用'
    __Use_nature_4 = '民用'
    #
    __Description_of_usage = '//input[@placeholder="请输入，非必填"]'

    __Building_Number_selector = '//textarea[@placeholder="请输入建筑层数"]'
    __Building_Area_selector = '//textarea[@placeholder="请输入建筑面积"]'
    __Total_Building_Area_selector = '//input[@placeholder="请输入建筑总面积"]'
    __Building_Height_selector = '//textarea[@placeholder="请输入建筑高度"]'
    __Building_volume_selector = '//input[@placeholder="请输入建筑体积"]'
    __Building_Construction_selector = '//input[@placeholder="请输入建筑结构"]'
    __Fire_level_selector = '//input[@placeholder="请输入耐火等级"]'
    __Hazard_Classification_selector = '//input[@placeholder="请输入"]'
    __Filing_date_selector = '//input[@placeholder="选择日期"]'
    # 建设单位
    __Construction_Unit_1 = '//input[@placeholder="请输入，支持模糊查询"]'
    __Construction_Unit_2 = '//div[@x-placement="bottom-start"]/div/div/ul/li/span[text()="滨州建设单位3210"]'
    # 技术负责人
    __Technical_leader_1 = '//form[@class="el-form form el-form--inline"]/div[16]/div[2]'
    __Technical_leader_2 = '//div[@x-placement="bottom-start"]/div/div/ul/li/span[text()="杨文明"]'

    __Temporarily_save_button_selector = '//div[@class="dialog-footer"]/button[1]'  # 暂存
    __Submit_button_selector = '//div[@class="dialog-footer"]/button[2]'  # 提交

    def goto_add_project(self):
        try:
            self._goto_url(self.__path)
            logger.info("Navigating to AddProject page")
        except Exception as e:
            logger.error(f"Failed to open AddProject page: {e}")
            raise

    def click_new_project_selector(self) -> None:
        try:
            self._click(self.__New_project_selector)
            logger.info("Clicking 新增项目")
        except Exception as e:
            logger.error(f"Failed to click 新增项目: {e}")
            raise

    def click_fire_inspection(self) -> None:
        try:
            self._click(self.__Fire_inspection_selector)
            logger.info("Clicking 消防验收")
        except Exception as e:
            logger.error(f"Failed to click 消防验收: {e}")
            raise

    def fill_project_name(self, value: str) -> None:
        try:
            self._fill(self.__Project_Name_selector, value)
            logger.info("Filling in 工程名称")
        except Exception as e:
            logger.error(f"Failed to fill 工程名称: {e}")
            raise

    def select_project_address(self) -> None:
        try:
            # self._fill_select(self.__Project_Address_1, *self.__Project_Address_2)
            self._select_options(self.__Project_Address_3, self.__Project_Address_4)
            logger.info("Selector 工程地址")
        except Exception as e:
            logger.error(f"Failed to Selector 工程地址：{e}")
            raise

    def select_category(self) -> None:
        try:
            self._fill_select(self.__category_1, *self.__category_2)
            self._click(self.__category_1)
            logger.info("Selector 类别")
        except Exception as e:
            logger.error(f"Failed to Selector 类别：{e}")
            raise

    def fill_building_number(self, value: str) -> None:
        try:
            self._fill(self.__Building_Number_selector, value)
            logger.info("Filling in 建筑层数")
        except Exception as e:
            logger.error(f"Failed to fill 建筑层数: {e}")
            raise

    def fill_building_height(self, value: str) -> None:
        try:
            self._fill(self.__Building_Height_selector, value)
            logger.info("Filling in 建筑高度")
        except Exception as e:
            logger.error(f"Failed to fill 建筑高度: {e}")
            raise

    def fill_building_area(self, value: str) -> None:
        try:
            self._fill(self.__Building_Area_selector, value)
            logger.info("Filling in 建筑面积")
        except Exception as e:
            logger.error(f"Failed to fill 建筑面积: {e}")
            raise

    def fill_total_building_area(self, value: str) -> None:
        try:
            self._fill(self.__Total_Building_Area_selector, value)
            logger.info("Filling in 建筑总面积")
        except Exception as e:
            logger.error(f"Failed to fill 建筑总面积: {e}")
            raise

    def fill_building_volume_selector(self, value: str) -> None:
        try:
            self._fill(self.__Building_volume_selector, value)
            logger.info("Filling in 建筑体积")
        except Exception as e:
            logger.error(f"Failed to fill 建筑体积: {e}")
            raise

    def select_use_nature(self) -> None:
        try:
            # self._fill_select(self.__Use_nature_1, *self.__Use_nature_2)
            self._select_options(self.__Use_nature_3, self.__Use_nature_4)
            logger.info("Selector 使用性质")
        except Exception as e:
            logger.error(f"Failed to Selector 使用性质：{e}")
            raise

    def fill_description_of_usage(self, value: str) -> None:
        try:
            self._fill(self.__Description_of_usage, value)
            logger.info("Filling in 使用性质说明")
        except Exception as e:
            logger.error(f"Failed to fill 使用性质说明: {e}")
            raise

    def fill_building_construction_selector(self, value: str) -> None:
        try:
            self._fill(self.__Building_Construction_selector, value)
            logger.info("Filling in 建筑结构")
        except Exception as e:
            logger.error(f"Failed to fill 建筑结构: {e}")
            raise

    def fill_fire_level(self, value: str) -> None:
        try:
            self._fill(self.__Fire_level_selector, value)
            logger.info("Filling in 耐火等级")
        except Exception as e:
            logger.error(f"Failed to fill 耐火等级: {e}")
            raise

    def fill_hazard_classification(self, value: str) -> None:
        try:
            self._fill(self.__Hazard_Classification_selector, value)
            logger.info("Filling in 建筑/火灾危险性分类")
        except Exception as e:
            logger.error(f"Failed to fill 建筑/火灾危险性分类: {e}")
            raise

    def click_filing_date_selector(self) -> None:
        try:
            self._select_date(self.__Filing_date_selector)
            logger.info("Clicking 建设单位申请消防备案时间")
        except Exception as e:
            logger.error(f"Failed to selector 建设单位申请消防备案时间：{e}")
            raise

    def select_construction_unit(self, value: str) -> None:
        try:
            self._fill_select(self.__Construction_Unit_1, self.__Construction_Unit_2, input_value=value)
            logger.info("建设单位")
        except Exception as e:
            logger.error(f"Failed to Selector 建设单位：{e}")
            raise

    def select_technical_leader(self) -> None:
        try:
            self._fill_select(self.__Technical_leader_1, self.__Technical_leader_2)
            logger.info("Selector 技术负责人")
        except Exception as e:
            logger.error(f"Failed to Selector 技术负责人：{e}")
            raise

    def click_temporarily_save_button(self) -> None:
        try:
            self._click(self.__Temporarily_save_button_selector)
            logger.info("Clicking 暂存按钮")
        except Exception as e:
            logger.error(f"Failed to click 暂存按钮: {e}")
            raise

    def click_submit_button(self) -> None:
        try:
            self._click(self.__Submit_button_selector)
            logger.info("Clicking 提交按钮")
        except Exception as e:
            logger.error(f"Failed to click 提交按钮: {e}")
            raise
