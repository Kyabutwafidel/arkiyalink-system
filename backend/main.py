from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import OpenAI

# Initialize client with environment variable
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

app = FastAPI(title='Arkiyalink AI API')

class Query(BaseModel):
    prompt: str

@app.post("/ai-query")
async def ai_query(q: Query):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": q.prompt}]
    )
    return {"answer": response.choices[0].message.content}
