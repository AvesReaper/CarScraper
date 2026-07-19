from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    context = browser.new_context()

    page = context.new_page()
    page.goto("https://playwright.dev/python/")



    # Print the page title
    print(page.title())
    # Print the first book's title
    page.locator("div.navbar__item > a:nth-child(1)").hover()
    page.locator(".dropdown__menu > li:nth-child(2) > a:nth-child(1)").click()
    # # Count the number of books on the page
    # print(page.locator("article.product_pod").count())

    # # Click the first book
    # page.locator("article.product_pod h3 a").first.click()

    page.close()