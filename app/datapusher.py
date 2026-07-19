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
