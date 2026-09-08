from langgraph.graph import StateGraph

from app.models.state import AgentState
from app.agents.job_extractor import extract_job
from app.agents.website_reader_agent import read_browser

from app.agents.eligiblity_checker import check_eligibility



builder=StateGraph(AgentState)

builder.add_node(
    "extract_job",
    extract_job
)
builder.add_node("read_website",read_browser)
builder.add_node("check_eligibility",check_eligibility)

builder.add_edge("extract_job","read_website")

builder.add_edge("read_website","check_eligibility")


builder.set_entry_point(
    "extract_job"
)

builder.set_finish_point(
    "check_eligibility"
)


graph=builder.compile()
