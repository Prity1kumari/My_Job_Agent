import json
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

def extract_form_fields(state):

    prompt = f"""
Extract all application form fields from this job application page.

Return ONLY JSON.

Format:

{{
    "fields":[]
}}

Page Content:

{state["website_content"]}
"""

    response = llm.invoke(prompt)

    content = response.content.strip()

    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()

    data = json.loads(content)

    return {
        **state,
        **data
    }