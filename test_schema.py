from app.services.form_schema_extractor import extract_form_schema

url = "https://www.rubrik.com/company/careers/departments/job.8166523?gh_jid=8166523&gh_src=hmy4uj221us"

schema = extract_form_schema(url)

print("\n\n===== FINAL SCHEMA =====\n")

for field in schema:
    print(field)