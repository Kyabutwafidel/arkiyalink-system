from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='Arki AI Mock API')

class Query(BaseModel):
    prompt: str

@app.post('/ai-query')
async def ai_query(q: Query):
    try:
        mock_answer = f"💡 Mock answer for your prompt: '{q.prompt}'"
        return {'answer': mock_answer}
    except Exception as e:
        return {'error': str(e)}
