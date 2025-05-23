import pytest
import requests
from dotenv import load_dotenv
import os

@pytest.fixture()
def create_token():
    load_dotenv()
    username=os.getenv("USERNAME")
    password=os.getenv("PASSWORD")
    print(username,password)
    print("creating token...")
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload={
        "username": username,
        "password": password
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    token = response.json()["token"]
    print(token)

    # Debug print
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    try:
        json_response = response.json()
        token = json_response["token"]
        return token
    except KeyError:
        pytest.fail(f"Token not found in response. Response was: {json_response}")
    except Exception as e:
        pytest.fail(f"Unexpected error: {e}")

@pytest.fixture()
def create_booking_id():
    print("Create booking id !")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response=requests.post(url=URL,headers=headers,json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))
    data=response.json()
    bookingid=data["bookingid"]
    return bookingid

@pytest.fixture
def read_csv_file_data():
    pass

@pytest.fixture
def read_mysql_file_database():
    pass

@pytest.fixture
def close_browser():
    print("Closing a browser!! Chrome")
    return "closed"

