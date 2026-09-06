from langgraph.graph import StateGraph

from app.models.state import AgentState
from app.agents.job_extractor import extract_job

builder=StateGraph(AgentState)

builder.add_node(
    "extract_job",
    extract_job
)


builder.set_entry_point(
    "extract_job"
)

builder.set_finish_point(
    "extract_job"
)


graph=builder.compile()
