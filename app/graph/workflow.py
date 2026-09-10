from langgraph.graph import StateGraph

from app.models.state import AgentState
from app.agents.job_extractor import extract_job
from app.agents.website_reader_agent import read_browser

from app.agents.eligiblity_checker import check_eligibility

from app.agents.platform_detector import detect_platform

from app.agents.form_filed_extractor import extract_form_fields



builder=StateGraph(AgentState)

builder.add_node(
    "extract_job",
    extract_job
)
builder.add_node("read_website",read_browser)
builder.add_node("check_eligibility",check_eligibility)
builder.add_node("detect_platform",detect_platform)

builder.add_node("extract_form_fields",extract_form_fields)

builder.add_edge("extract_job","read_website")

builder.add_edge("read_website","check_eligibility")

builder.add_edge("check_eligibility","detect_platform")

builder.add_edge("detect_platform","extract_form_fields")




builder.set_entry_point(
    "extract_job"
)

builder.set_finish_point(
    "extract_form_fields"
)


graph=builder.compile()
