from playwright.sync_api import sync_playwright

def read_page(url: str):

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=60000
        )

        page.wait_for_timeout(5000)

        print("TITLE:", page.title())
        print("URL:", page.url)

        fields = page.locator(
            "input, textarea, select"
        ).evaluate_all(
            """
            elements => elements.map(
                e => ({
                    name: e.name,
                    type: e.type,
                    placeholder: e.placeholder
                })
            )
            """
        )

        print("\n=== FORM FIELDS ===")
        for field in fields:
            print(field)

        page.screenshot(
            path="debug.png",
            full_page=True
        )

        content = page.locator("body").inner_text()

        browser.close()

        return {
            "content": content,
            "fields": fields
        }