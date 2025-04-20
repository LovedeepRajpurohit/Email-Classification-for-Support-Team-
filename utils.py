import re

def mask_pii(email_body: str):
    masked_entities = []

    # Regex patterns for PII
    pii_patterns = {
        "EMAIL": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "PHONE": r"\+?[0-9]{1,3}[-.\s]?[0-9]{1,4}[-.\s]?[0-9]{1,4}[-.\s]?[0-9]{1,9}",
        "NAME": r"\b[A-Z][a-z]*\s[A-Z][a-z]*\b"
    }

    # Replace PII with placeholders
    for pii_type, pattern in pii_patterns.items():
        matches = re.finditer(pattern, email_body)
        for match in matches:
            start, end = match.start(), match.end()
            original_value = email_body[start:end]
            masked_entities.append({
                "position": [start, end],
                "classification": pii_type,
                "entity": original_value
            })
            email_body = email_body[:start] + f"<{pii_type}>" + email_body[end:]

    return email_body, masked_entities