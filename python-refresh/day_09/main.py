from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Lead(BaseModel):
    # if you want company to be optional for example, do "company: str | None = None"
    name: str
    email: str
    company: str
    message: str

@app.post("/webhook/lead")
def process_lead(lead: Lead):
    print("NEW LEAD")
    print(f"Name: {lead.name}")
    print(f"Email: {lead.email}")
    print(f"Company: {lead.company}")
    print(f"Message: {lead.message}")
    
    response = {
        "success": True,
        "message": "Lead processed successfully."
    }

    return response
