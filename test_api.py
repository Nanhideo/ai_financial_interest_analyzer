import requests
import json

url = "http://localhost:8000/api/calculate"
payload = {
    "name": "John Doe",
    "amount": 10000,
    "interest_rate": 5.5,
    "months": 12,
    "monthly_contribution": 500
}

response = requests.post(url, json=payload)
print(f"Status Code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")
