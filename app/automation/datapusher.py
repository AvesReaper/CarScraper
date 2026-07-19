import requests


def sendtodb(payload):
    url = "http://localhost:8000/cars"


    try:
        response = requests.post(url, json=payload)

        print(f"Status Code: {response.status_code}")

        if response.ok:
            print("Response JSON:")
            print(response.json())
        else:
            print("Error:")
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    
    return response.status_code


test_pay = {
  "brand": "BMW",
  "model": "720ld",
  "year": 2007,
  "price": 100000,
  "fuel_type": "diesel",
  "transmission": "AWD",
  "kilometers": 200000
}

print(sendtodb(test_pay))