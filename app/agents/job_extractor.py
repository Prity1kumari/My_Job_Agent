import json

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

def extract_job(state):

    prompt = f"""
Extract information from this job post.

Return ONLY JSON.

Job Post:
{state['raw_job_post']}

Format:

{{
  "company":"",
  "role":"",
  "apply_url":"",
  "apply_method":"website/email",
  "eligible": true
}}
"""

    response = llm.invoke(prompt)

    print("===== GEMINI RESPONSE =====")
    print(response.content)
    print("===========================")

    content = response.content.strip()

    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()

    data = json.loads(content)

    return {
        **state,
        **data
    }