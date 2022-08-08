import uuid


def generate_email():
    return f"{str(uuid.uuid4())[:8]}@mailinator.com"
