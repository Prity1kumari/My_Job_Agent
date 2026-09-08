from app.services.browser_service import read_page
from app.models.state import AgentState



def read_browser(state):

    content=read_page(
        state["apply_url"]
    )

    return{
        **state,
        "website_content":content
    }