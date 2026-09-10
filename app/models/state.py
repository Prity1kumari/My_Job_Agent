from typing import TypedDict

class AgentState(TypedDict,total=False):
    raw_job_post:str
    company:str
    role:str
    apply_url:str
    apply_method:str
    eligible:bool
    website_content:str
    eligible:bool
    reason:str
    platform:str
    auto_apply_supported:bool

    fields:list

