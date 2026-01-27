
import os
from playwright.sync_api import sync_playwright, expect

def verify_gift_ui():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the local index.html file
        file_path = os.path.abspath("index.html")
        page.goto(f"file://{file_path}")

        # 1. Switch to Supplements Tab
        page.click("#tab-supplements")

        # 2. Select all add-ons to trigger the gift
        # Using class selector as defined in HTML
        addons = page.locator(".supp-addon")
        count = addons.count()
        print(f"Found {count} addons")

        for i in range(count):
            addons.nth(i).check()

        # 3. Wait for gift section to appear
        gift_section = page.locator("#supp-gift-section")
        expect(gift_section).to_be_visible(timeout=5000)

        # 4. Assertions

        # Check for L-CARNITINA text
        expect(gift_section).to_contain_text("L-CARNITINA")

        # Check for GRATIS tag
        expect(gift_section).to_contain_text("¡GRATIS!")

        # Check that "Valor Real" is NOT present (using page content check within the section)
        content = gift_section.inner_text()
        if "Valor Real" in content:
            print("FAILURE: 'Valor Real' text found in gift section!")
        else:
            print("SUCCESS: 'Valor Real' text correctly removed.")

        # 5. Take Screenshot
        # We wait a bit for animations to settle
        page.wait_for_timeout(1000)
        screenshot_path = "/home/jules/verification/gift_ui_update.png"
        gift_section.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    verify_gift_ui()
