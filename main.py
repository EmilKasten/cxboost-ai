from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import openai
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate")
async def generate_response(request: Request, ticket: str = Form(...)):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Du bist ein professioneller Kundenservice-Agent."},
                {"role": "user", "content": f"Dies ist eine Kundenanfrage: '{ticket}'. Was ist die passende Antwort?"}
            ]
        )
        answer = completion.choices[0].message["content"].strip()
        return templates.TemplateResponse("index.html", {
            "request": request,
            "ticket": ticket,
            "response": answer
        })
    except Exception as e:
        return HTMLResponse(content=f"Fehler: {str(e)}", status_code=500)