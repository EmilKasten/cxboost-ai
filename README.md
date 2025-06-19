# CXBoost-AI (Hosted Demo)

Ein KI-basierter Kundenservice-Agent, der mit GPT-4o Antworten auf Kundenanfragen generiert.

## Installation

1. `pip install -r requirements.txt`
2. Setze deinen OpenAI API-Key als Umgebungsvariable:
   `export OPENAI_API_KEY=dein-api-key`

3. Starte den Server:
   `uvicorn main:app --reload`

## Nutzung

- Öffne im Browser: http://localhost:8000
- Gib eine Kundenanfrage ein
- Der Agent generiert automatisch eine Antwort

## Deployment

Empfohlen: [Render.com](https://render.com) oder [Vercel](https://vercel.com)