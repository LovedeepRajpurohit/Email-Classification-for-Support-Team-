from fastapi import FastAPI
from pydantic import BaseModel
from models import classify_email
from utils import mask_pii

# Initialize FastAPI app
app = FastAPI()

# Define request model
class EmailRequest(BaseModel):
    email_body: str

# Define response model
class EmailResponse(BaseModel):
    input_email_body: str
    list_of_masked_entities: list
    masked_email: str
    category_of_the_email: str

@app.post("/classify", response_model=EmailResponse)
def classify_email_api(request: EmailRequest):
    email_body = request.email_body

    # Mask PII in the email body
    masked_email, masked_entities = mask_pii(email_body)

    # Classify the email category
    category = classify_email(masked_email)

    # Prepare the response
    response = EmailResponse(
        input_email_body=email_body,
        list_of_masked_entities=masked_entities,
        masked_email=masked_email,
        category_of_the_email=category,
    )
    return response