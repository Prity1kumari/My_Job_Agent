from playwright.sync_api import sync_playwright


def extract_form_schema(url: str):

    schema = []

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

        print("\n===== EXTRACTING FORM SCHEMA =====\n")

        # -----------------------
        # INPUT FIELDS
        # -----------------------

        inputs = page.locator("input").all()

        for field in inputs:

            field_type = field.get_attribute("type")

            if field_type in ["hidden", "submit", "search"]:
                continue

            field_id = field.get_attribute("id")

            label = None

            if field_id:
                try:
                    label = page.locator(
                        f"label[for='{field_id}']"
                    ).inner_text()
                except:
                    pass

            item = {
                "label": label,
                "name": field.get_attribute("name"),
                "id": field_id,
                "type": field_type,
                "required": field.get_attribute("required")
                is not None
            }

            print(item)

            schema.append(item)

        # -----------------------
        # TEXTAREA
        # -----------------------

        textareas = page.locator("textarea").all()

        for field in textareas:

            field_id = field.get_attribute("id")

            label = None

            if field_id:
                try:
                    label = page.locator(
                        f"label[for='{field_id}']"
                    ).inner_text()
                except:
                    pass

            item = {
                "label": label,
                "name": field.get_attribute("name"),
                "id": field_id,
                "type": "textarea",
                "required": field.get_attribute("required")
                is not None
            }

            print(item)

            schema.append(item)

        # -----------------------
        # SELECT
        # -----------------------

        selects = page.locator("select").all()

        for field in selects:

            field_id = field.get_attribute("id")

            label = None

            if field_id:
                try:
                    label = page.locator(
                        f"label[for='{field_id}']"
                    ).inner_text()
                except:
                    pass

            options = field.locator(
                "option"
            ).all_inner_texts()

            item = {
                "label": label,
                "name": field.get_attribute("name"),
                "id": field_id,
                "type": "select",
                "options": options,
                "required": field.get_attribute("required")
                is not None
            }

            print(item)

            schema.append(item)

        browser.close()

    return schema