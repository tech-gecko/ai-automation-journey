import requests

headers = {
    "Content-Type": "application/json"
}
valid_lead1 = {
    "name": "John Doe",
    "email": "john@example.com",
    "company": "ABC Ltd",
    "message": "I need an automation system."
}
missing_company = {
    "name": "John Doe",
    "email": "john@example.com",
    "message": "I need an automation system."
}
invalid_json = [
    "name: John Doe",
    "email: john@example.com",
    "company: ABC Ltd",
    "message: I need an automation system."
]
valid_lead2 = {
    "name": "Sarah Williams",
    "email": "sarah@example.com",
    "company": "XYZ Solutions",
    "message": "We want to automate our customer follow-up process."
}

response1 = requests.post("http://127.0.0.1:8000/webhook/lead", json=valid_lead1, headers=headers).json()
response2 = requests.post("http://127.0.0.1:8000/webhook/lead", json=missing_company, headers=headers).json()
response3 = requests.post("http://127.0.0.1:8000/webhook/lead", json=invalid_json, headers=headers).json()
response4 = requests.post("http://127.0.0.1:8000/webhook/lead", json=valid_lead2, headers=headers).json()

print(response1)
print(response2)
print(response3)
print(response4)
