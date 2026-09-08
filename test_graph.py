from app.graph.workflow import graph

result = graph.invoke(
    {
        "raw_job_post": """
        Rubrik is hiring Software Engineer - Winter Intern.

        Apply:
        https://www.rubrik.com/company/careers/departments/job.8166523?gh_jid=8166523&gh_src=hmy4uj221us
        """
    }
)

print(result)