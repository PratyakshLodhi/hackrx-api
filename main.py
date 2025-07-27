from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Request model
class RunQueryRequest(BaseModel):
    documents: str
    questions: List[str]

# Response model
class RunQueryResponse(BaseModel):
    answers: List[str]

# Dummy logic (to be replaced with real RAG later)
def dummy_query_answering(document_url: str, questions: List[str]) -> List[str]:
    return ["Hello, World!"] * len(questions)

# POST endpoint
@app.post("/hackrx/run", response_model=RunQueryResponse)
async def run_query(
    payload: RunQueryRequest,
    authorization: str = Header(None)
):
    # Token check (for HackRx requirement)
    valid_token = "a18194ed79ce2d73374be4d9d8067ca39fb7b72f1a02a5f4fb170ae3dc79ac9"
    if authorization != f"Bearer {valid_token}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    answers = dummy_query_answering(payload.documents, payload.questions)
    return {"answers": answers}

# Optional: Needed by Render's Start Command
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=10000)
