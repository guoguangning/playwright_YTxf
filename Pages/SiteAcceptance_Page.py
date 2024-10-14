"""
-*- coding: utf-8 -*-
@File    : SiteAcceptance_Page.py
@Date    : 2024/10/9 15:01
@Author  : ggn
"""
from BasePage.BasePage import BasePage
from BasePage.logger import Logger
from Utils.Utils_yaml import load_yaml

logger = Logger("SiteAcceptance_Page").get_log()


class SiteAcceptancePage(BasePage):
    SiteAcceptancePage_data = load_yaml(r'C:\case\playwright-YTxf\TestDatas\EleData\SiteAcceptance_Page.yaml')

    def goto_site_acceptance(self):
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

    def click_site_acceptance(self) -> None:
        try:
            self._click(self.SiteAcceptancePage_data['__site_acceptance'])
            logger.info("Click 现场验收")
        except Exception as e:
            logger.error(f"Failed to Click 现场验收失败: {e}")
            raise

    def select_table_1(self, value, value2, files) -> None:
        try:
            self._click(self.SiteAcceptancePage_data['__Table_1'])
            self._click(self.SiteAcceptancePage_data['__Table_1_Conclusions'])

            self._fill(self.SiteAcceptancePage_data['__Table_1_Opinions'], value)
            self._click(self.SiteAcceptancePage_data['__Table_1_Opinion_Images'])
            self._file(self.SiteAcceptancePage_data['__Table_1_Opinion_Images_input'], files)
            self._click(self.SiteAcceptancePage_data['__Table_1_Opinion_Images_save'])

            self._click(self.SiteAcceptancePage_data['__Table_1_Add_acceptance_comments'])
            self._fill(self.SiteAcceptancePage_data['__Table_1_Opinions_2'], value2)
            logger.info("Select 建筑类别与耐火等级验收结论选择完毕")
        except Exception as e:
            logger.error(f"Failed to Select 建筑类别与耐火等级验收结论选择失败: {e}")
            raise

    def select_table_1_pass(self) -> None:
        try:
            self._click(self.SiteAcceptancePage_data['__Table_1'])
            self._click(self.SiteAcceptancePage_data['__Table_1_Conclusion'])
            logger.info("Select 建筑类别与耐火等级验收结论选择完毕")
        except Exception as e:
            logger.error(f"Failed to Select 建筑类别与耐火等级验收结论选择失败: {e}")
            raise

    def select_table_1_2(self, value, value2) -> None:
        """第二次现场验收"""
        try:
            self._click(self.SiteAcceptancePage_data['__Table_1_Conclusion2'])
            self._fill(self.SiteAcceptancePage_data['__Table_1_Opinions2'], value)

            self._click(self.SiteAcceptancePage_data['__Table_1_Conclusion3'])

            self._click(self.SiteAcceptancePage_data['__Table_1_Add_acceptance_comments'])
            self._fill(self.SiteAcceptancePage_data['__Table_1_Opinions3'], value2)
            logger.info("Select 二次建筑类别与耐火等级验收结论选择完毕")
        except Exception as e:
            logger.error(f"Failed to Select 二次建筑类别与耐火等级验收结论选择失败: {e}")
            raise

    def select_table_1_3(self) -> None:
        """第三次现场验收"""
        try:
            self._click(self.SiteAcceptancePage_data['__Table_1_Conclusion4'])
            self._click(self.SiteAcceptancePage_data['__Table_1_Conclusion5'])
            logger.info("Select 三次建筑类别与耐火等级验收结论选择完毕")
        except Exception as e:
            logger.error(f"Failed to Select 三次建筑类别与耐火等级验收结论选择失败: {e}")
            raise

    def select_table_2(self) -> None:
        try:
            self._click(self.SiteAcceptancePage_data['__Table_2'])
            self._click(self.SiteAcceptancePage_data['__Table_2_Conclusion'])
            logger.info("Select 总平面布局结论选择完毕")
        except Exception as e:
            logger.error(f"Failed to Select 总平面布局结论选择失败: {e}")
            raise

    def select_table_3(self) -> None:
        try:
            self._click(self.SiteAcceptancePage_data['__Table_3'])
            self._click(self.SiteAcceptancePage_data['__Table_3_Conclusion'])
            logger.info("Select 平面布置结论选择完毕")
        except Exception as e:
            logger.error(f"Failed to Select 平面布置结论选择失败: {e}")
            raise

    def select_table_4(self) -> None:
        try:
            self._click(self.SiteAcceptancePage_data['__Table_4'])
            self._click(self.SiteAcceptancePage_data['__Table_4_Conclusion'])
            logger.info("Select 建筑外墙、屋面保温和建筑外墙装饰结论选择完毕")
        except Exception as e:
            logger.error(f"Failed to Select 建筑外墙、屋面保温和建筑外墙装饰结论选择失败: {e}")
            raise

    def select_table_5(self) -> None:
        try:
            self._click(self.SiteAcceptancePage_data['__Table_5'])
            self._click(self.SiteAcceptancePage_data['__Table_5_Conclusion'])
            logger.info("Select 建筑内部装修防火结论选择完毕")
        except Exception as e:
            logger.error(f"Failed to Select 建筑内部装修防火结论选择失败: {e}")
            raise

    def select_table_6(self) -> None:
        try:
            self._click(self.SiteAcceptancePage_data['__Table_6'])
            self._click(self.SiteAcceptancePage_data['__Table_6_Conclusion'])
            logger.info("Select 防火分隔结论选择完毕")
        except Exception as e:
            logger.error(f"Failed to Select 防火分隔结论选择失败: {e}")
            raise

    def select_table_7(self) -> None:
        try:
            self._click(self.SiteAcceptancePage_data['__Table_7'])
            self._click(self.SiteAcceptancePage_data['__Table_7_Conclusion'])
            logger.info("Select 防爆结论选择完毕")
        except Exception as e:
            logger.error(f"Failed to Select 防爆结论选择失败: {e}")
            raise

    def select_table_8(self) -> None:
        try:
            self._click(self.SiteAcceptancePage_data['__Table_8'])
            self._click(self.SiteAcceptancePage_data['__Table_8_Conclusion'])
            logger.info("Select 安全疏散结论选择完毕")
        except Exception as e:
            logger.error(f"Failed to Select 安全疏散结论选择失败: {e}")
            raise

    def select_table_9(self) -> None:
        try:
            self._click(self.SiteAcceptancePage_data['__Table_9'])
            self._click(self.SiteAcceptancePage_data['__Table_9_Conclusion'])
            logger.info("Select 消防电梯结论选择完毕")
        except Exception as e:
            logger.error(f"Failed to Select 消防电梯结论选择失败: {e}")
            raise

    def select_table_10(self) -> None:
        try:
            self._click(self.SiteAcceptancePage_data['__Table_10'])
            self._click(self.SiteAcceptancePage_data['__Table_10_Conclusion'])
            logger.info("Select 消火栓系统结论选择完毕")
        except Exception as e:
            logger.error(f"Failed to Select 消火栓系统结论选择失败: {e}")
            raise

    def select_table_11(self) -> None:
        try:
            self._click(self.SiteAcceptancePage_data['__Table_11'])
            self._click(self.SiteAcceptancePage_data['__Table_11_Conclusion'])
            logger.info("Select 自动喷水灭火系统结论选择完毕")
        except Exception as e:
            logger.error(f"Failed to Select 自动喷水灭火系统结论选择失败: {e}")
            raise

    def select_table_12(self) -> None:
        try:
            self._click(self.SiteAcceptancePage_data['__Table_12'])
            self._click(self.SiteAcceptancePage_data['__Table_12_Conclusion'])
            logger.info("Select 火灾自动报警系统结论选择完毕")
        except Exception as e:
            logger.error(f"Failed to Select 火灾自动报警系统结论选择失败: {e}")
            raise

    def select_table_13(self) -> None:
        try:
            self._click(self.SiteAcceptancePage_data['__Table_13'])
            self._click(self.SiteAcceptancePage_data['__Table_13_Conclusion'])
            logger.info("Select 防烟排烟系统及通风、空调系统防火结论选择完毕")
        except Exception as e:
            logger.error(f"Failed to Select 防烟排烟系统及通风、空调系统防火结论选择失败: {e}")
            raise

    def select_table_14(self) -> None:
        try:
            self._click(self.SiteAcceptancePage_data['__Table_14'])
            self._click(self.SiteAcceptancePage_data['__Table_14_Conclusion'])
            logger.info("Select 消防电气结论选择完毕")
        except Exception as e:
            logger.error(f"Failed to Select 消防电气结论选择失败: {e}")
            raise

    def select_table_15(self) -> None:
        try:
            self._click(self.SiteAcceptancePage_data['__Table_15'])
            self._click(self.SiteAcceptancePage_data['__Table_15_Conclusion'])
            logger.info("Select 建筑灭火器结论选择完毕")
        except Exception as e:
            logger.error(f"Failed to Select 建筑灭火器结论选择失败: {e}")
            raise

    def submit(self) -> None:
        try:
            self._click(self.SiteAcceptancePage_data['__Submit_button'])
            self._click(self.SiteAcceptancePage_data['__Double_confirmation_button'])
            logger.info("Submit 验收结论完毕 ")
        except Exception as e:
            logger.error(f"Failed to Submit 验收结论失败: {e}")
            raise
