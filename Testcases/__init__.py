# import pytest
# from playwright.sync_api import sync_playwright
#
#
# @pytest.fixture(scope="module")
# def browser():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, args=['--start-maximized'])
#         yield browser
#         browser.close()
#
#
# @pytest.fixture(scope="function")
# def page(browser):
#     context = browser.new_context(no_viewport=True)
#     page = context.new_page()
#     yield page
#     context.close()
