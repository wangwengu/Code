from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to about:blank
    page.goto("about:blank")

    # Go to https://www.cambly.com/english?lang=zh_CN
    page.goto("https://www.cambly.com/english?lang=zh_CN")

    # Click text=登录
    # with page.expect_navigation(url="https://www.cambly.com/student/login?lang=zh_CN"):
    with page.expect_navigation():
        page.click("text=登录")
    # assert page.url == "https://www.cambly.com/student/login"

    # Click button:has-text("Apple")
    with page.expect_popup() as popup_info:
        page.click("button:has-text(\"Apple\")")
    page1 = popup_info.value

    # Fill input[type="text"]
    page1.fill("input[type=\"text\"]", "1339732832@qq.com")

    # Press Enter
    page1.press("input[type=\"text\"]", "Enter")

    # Fill input[type="password"]
    page1.fill("input[type=\"password\"]", "371324neT")

    # Press Enter
    page1.press("input[type=\"password\"]", "Enter")

    # Fill [aria-label="Enter\ verification\ code\.\ After\ entering\ the\ verification\ code\,\ the\ page\ gets\ updated\ automatically\.\ 位\ 1"]
    page1.fill("[aria-label=\"Enter\\ verification\\ code\\.\\ After\\ entering\\ the\\ verification\\ code\\,\\ the\\ page\\ gets\\ updated\\ automatically\\.\\ 位\\ 1\"]", "6")

    # Fill [aria-label="位\ 2"]
    page1.fill("[aria-label=\"位\\ 2\"]", "1")

    # Fill [aria-label="位\ 3"]
    page1.fill("[aria-label=\"位\\ 3\"]", "9")

    # Fill [aria-label="位\ 4"]
    page1.fill("[aria-label=\"位\\ 4\"]", "3")

    # Fill [aria-label="位\ 5"]
    page1.fill("[aria-label=\"位\\ 5\"]", "2")

    # Fill [aria-label="位\ 6"]
    page1.fill("[aria-label=\"位\\ 6\"]", "6")

    # Click #trust-browser-1644839634565-4
    page1.click("#trust-browser-1644839634565-4")

    # Click button:has-text("继续")
    page1.click("button:has-text(\"继续\")")

    # Close page
    page1.close()

    # Go to https://www.cambly.com/en/student
    page.goto("https://www.cambly.com/en/student")

    # Go to https://www.cambly.com/en/student?lang=zh_CN
    page.goto("https://www.cambly.com/en/student?lang=zh_CN")

    # Click text=私人教师
    page.click("text=私人教师")
    # assert page.url == "https://www.cambly.com/en/student/tutors"

    # Click text=收藏
    page.click("text=收藏")
    # assert page.url == "https://www.cambly.com/en/student/tutors?#tab=favorites"

    # Click text=Craig D'Aurizio
    # with page.expect_navigation(url="https://www.cambly.com/en/student/tutors/6040525b0a6d581c8832223a?lang=zh_CN"):
    with page.expect_navigation():
        with page.expect_popup() as popup_info:
            page.click("text=Craig D'Aurizio")
        page2 = popup_info.value

    # Click button:has-text("15")
    page2.click("button:has-text(\"15\")")

    # Click text=返回
    page2.click("text=返回")

    # Click button:has-text("17")
    page2.click("button:has-text(\"17\")")

    # Click text=返回
    page2.click("text=返回")

    # Click button:has-text("19")
    page2.click("button:has-text(\"19\")")

    # Click text=返回
    page2.click("text=返回")

    # Click button:has-text("21")
    page2.click("button:has-text(\"21\")")

    # Click text=返回
    page2.click("text=返回")

    # Click button:has-text("23")
    page2.click("button:has-text(\"23\")")

    # Click text=返回
    page2.click("text=返回")

    # Click button:has-text("25")
    page2.click("button:has-text(\"25\")")

    # Click text=返回
    page2.click("text=返回")

    # Click button:has-text("26")
    page2.click("button:has-text(\"26\")")

    # Click text=返回
    page2.click("text=返回")

    # Click button:has-text("17")
    page2.click("button:has-text(\"17\")")

    # Click button:has-text("选择")
    page2.click("button:has-text(\"选择\")")

    # Select 30
    page2.select_option("text=--1530 分钟 >> select", "30")

    # 
    page2.click("text=22:00 - 22:30选择 >> button")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
