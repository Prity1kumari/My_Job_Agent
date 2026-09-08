from typing import TypedDict

class AgentState(TypedDict):
    raw_job_post:str
    company:str
    role:str
    apply_url:str
    apply_method:str
    eligible:bool
    website_content:str
    eligible:bool
    reason:str

