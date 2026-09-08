import json

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)


def check_eligibility(state):

    candidate_profile = """
    Candidate Profile:

    Name: Prity Kumari
    Degree: B.Tech
    Branch: Computer Scinece and Engineering (CSE)
    Graduation Year: 2027
    CGPA: 8.61
    """

    prompt = f"""
    You are an expert recruiter.

    Determine whether the candidate is eligible.

    {candidate_profile}

    Job Description:

    {state["website_content"]}

    Return ONLY valid JSON.

    {{
        "eligible": true,
        "reason": "short reason"
    }}
    """

    response = llm.invoke(prompt)

    content = response.content.strip()
    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()

    try:
        data = json.loads(content)

        return {
            **state,
            "eligible": data["eligible"],
            "reason": data["reason"]
        }

    except Exception as e:

        print("Eligibility Parse Error:", e)
        print(content)

        return {
            **state,
            "eligible": False,
            "reason": "Unable to determine eligibility"
        }