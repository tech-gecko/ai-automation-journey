import requests

webhook_url = "http://localhost:5678/webhook-test/lead-intake"

headers = {
    "Content-Type": "application/json"
}

valid_lead1 = {
  "name": "   TechGEcko   ",
  "email": "  Tech_Gecko@example.com   ",
  "company": " Forex Gecko    ",
  "message": "     We want to automate our trade journaling.    "
}

response = requests.post(webhook_url, json=valid_lead1, headers=headers).json()

print(response)
