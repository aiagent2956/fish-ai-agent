from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {
        "status": "Fish AI Agent is running successfully"
    }

@app.post("/chat")
def chat(request: ChatRequest):

    user_message = request.message.lower()

    if "fingerlings" in user_message:
        reply = "Yes, we have healthy fingerlings available from Kaduna. How many pieces do you need?"

    elif "juveniles" in user_message:
        reply = "We currently have quality juveniles ready for stocking. Please tell me your quantity."

    elif "jumbo" in user_message:
        reply = "Our jumbo catfish are available for harvest and supply. Kindly specify the quantity you want."

    elif "smoked" in user_message:
        reply = "Our premium smoked catfish can last up to one year when stored properly. Would you like to place an order?"

    elif "crayfish" in user_message:
        reply = "Yes, we supply fresh crayfish in different quantities. Kindly tell us how much you need."

    else:
        reply = "Welcome to Fish Planet and More. We sell fingerlings, juveniles, jumbo catfish, premium smoked catfish and crayfish. How can we assist you today?"

    return {
        "response": reply
    }
