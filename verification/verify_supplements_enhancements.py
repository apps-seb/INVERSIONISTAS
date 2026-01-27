from playwright.sync_api import sync_playwright
import time
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1280, 'height': 800})
        page = context.new_page()

        # Load local file
        page.goto(f"file://{os.getcwd()}/index.html")

        # Scroll to demo section
        page.locator("#demo-compra").scroll_into_view_if_needed()
        time.sleep(1)

        # Switch to Supplements Tab
        page.click("#tab-supplements")
        time.sleep(1)

        # Verify Expectation Message
        expectation = page.get_by_text("RETO FITNESS")
        assert expectation.is_visible(), "Expectation message 'RETO FITNESS' not visible"
        print("Expectation message verified.")

        # Select All Addons
        addons = page.locator(".supp-addon")
        count = addons.count()
        for i in range(count):
            addons.nth(i).check()
            time.sleep(0.1)

        # Verify Gift Unlocked with new styling
        gift_section = page.locator("#supp-gift-section")
        assert gift_section.is_visible(), "Gift Section not visible"

        # Verify new title styling (approximate check by text content)
        title = page.locator("#supp-gift-section p").first
        assert "OBSEQUIO DESBLOQUEADO" in title.inner_text()
        print("Gift title content verified.")

        # Verify value text
        value_text = page.locator("#supp-gift-section").get_by_text("Valor Real:")
        assert value_text.is_visible()
        print("Value text verified.")

        # Screenshot
        page.screenshot(path="verification/supplements_final.png")
        print("Screenshot saved to verification/supplements_final.png")

        browser.close()

if __name__ == "__main__":
    run()
