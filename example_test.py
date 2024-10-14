import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://192.168.10.230:30510/login")
    page.get_by_placeholder("请输入账号").click(modifiers=["ControlOrMeta"])
    page.get_by_placeholder("请输入账号").fill("13723945525")
    page.get_by_placeholder("请输入密码").click(modifiers=["ControlOrMeta"])
    page.get_by_placeholder("请输入密码").fill("Th#VHv1P6T3s53Ug")
    page.get_by_role("button", name="登录").click()
    page.locator("div").filter(has_text=re.compile(r"^新增项目$")).click()
    page.get_by_role("link", name="消防验收").click()
    page.get_by_placeholder("选择日期").click()
    page.get_by_text("14").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
