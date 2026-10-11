import requests

webhook_url = "http://localhost:5678/webhook-test/lead-intake"

headers = {
  "Content-Type": "application/json"
}

valid_lead1 = {
  "name": "   TUNDE   BALOGUN   ",
  "email": "  TUNDE.TEST06@EXAMPLE.COM  ",
  "company": "   BALOGUN FOODS   ",
  "message": "Following up on the support issue we reported previously."
}

response = requests.post(webhook_url, json=valid_lead1, headers=headers).json()
print(response)
