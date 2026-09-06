from fastapi import APIRouter

from app.graph.workflow import graph


router=APIRouter()

@router.post("/analyze")
def analyze(payload:dict):

    result=graph.invoke(
        {
            "raw_job_post":payload["job_post"]
        }
    )

    return result

