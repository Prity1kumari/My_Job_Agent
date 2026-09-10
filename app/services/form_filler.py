from playwright.sync_api import sync_playwright

def fill_form(url:str):

    with sync_playwright() as p:

        browser=p.chromium.launch(
            headless=False
        )

        page=browser.new_page()

        page.goto(
            url,
            wait_until="domcontentloaded"
        )

        page.wait_for_timeout(5000)

        try:
            page.locator("input[name*=first]").fill("Prity")
        except:
            pass


        try:

            page.locator("input[name*=last]").fill("kumari") 

        except:
            pass

        try:
            page.locator("input[type=email]").fill(
                "prity.cse.23@nitap.ac.in"
            )
        except:
            pass

        # Phone
        try:
            page.locator("input[type=tel]").fill(
                "8986525020"
            )
        except:
            pass

        page.screenshot(
            path="filled_form.png",
            full_page=True
        )

        print("FORM FILLED")

        input("Press Enter to close browser...")

        browser.close()


               