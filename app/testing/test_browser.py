from services.browser_service import read_page

url = "https://www.rubrik.com/company/careers/departments/job.8166523?gh_jid=8166523&gh_src=hmy4uj221us"

content = read_page(url)

print(content[:3000])