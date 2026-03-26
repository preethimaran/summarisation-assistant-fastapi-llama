from fastapi import APIRouter
from pydantic import BaseModel
from app.models.summariser import text_summariser
from app.utils.fetch import get_content

router = APIRouter()

class RequestBody(BaseModel):
    url: str | None = None
    text: str | None = None

@router.post("/summarise")
def process_request(request: RequestBody):
    if request.url != "":
        content = get_content(request.url)
        if content == "ERROR!!!":
            return {"summary": ""}
    elif request.text != "":
        content = request.text
    else:
        return{"error": "Provide either an URL or text to summarise"}
    
    summary = text_summariser(content)
    return {"summary": summary}