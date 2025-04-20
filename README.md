# Email Classification for Support Teams

## Overview
This project implements:
- **PII Masking**: Identifies and masks personal information in emails.
- **Email Classification**: Classifies emails into predefined support categories using a Naïve Bayes model.
- **API Deployment**: Exposes an endpoint to process and classify emails.

---

## Setup Instructions

### Prerequisites
- Python 3.8 or above
- Pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/LovedeepRajpurohit/Email-Classification-for-Support-Team-.git
   cd Email-Classification-for-Support-Team-
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Train the model:
   ```bash
   python models.py
   ```

4. Run the API:
   ```bash
   uvicorn api:app --reload
   ```

---

## API Usage

### Endpoint
**POST** `/classify`

### Request Format
```json
{
  "email_body": "string containing the email"
}
```

### Response Format
```json
{
  "input_email_body": "string containing the email",
  "list_of_masked_entities": [
    {
      "position": [start_index, end_index],
      "classification": "entity_type",
      "entity": "original_entity_value"
    }
  ],
  "masked_email": "string containing the masked email",
  "category_of_the_email": "string containing the class"
}
```

### Example
#### Request
```json
{
  "email_body": "Hello, my name is John Doe. You can reach me at john.doe@example.com or +1-555-123-4567."
}
```

#### Response
```json
{
  "input_email_body": "Hello, my name is John Doe. You can reach me at john.doe@example.com or +1-555-123-4567.",
  "list_of_masked_entities": [
    {
      "position": [18, 26],
      "classification": "NAME",
      "entity": "John Doe"
    },
    {
      "position": [40, 58],
      "classification": "EMAIL",
      "entity": "john.doe@example.com"
    },
    {
      "position": [62, 75],
      "classification": "PHONE",
      "entity": "+1-555-123-4567"
    }
  ],
  "masked_email": "Hello, my name is <NAME>. You can reach me at <EMAIL> or <PHONE>.",
  "category_of_the_email": "Incident"
}
```

---

## Deployment

The application is deployed on Hugging Face Spaces. Access the live endpoint here:
[Hugging Face Spaces Deployment Link](#)

---