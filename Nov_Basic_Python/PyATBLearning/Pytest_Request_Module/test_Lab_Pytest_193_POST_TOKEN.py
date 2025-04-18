import pytest
import allure
import requests

# pip install pytest allure requests

# Create Token - POST
base_url = "https://restful-booker.herokuapp.com"
headers = {"Content-Type": "application/json"}

#verify the token using authorization
def get_token():
    base_path = "/auth"
    full_url = base_url + base_path
    json_payload_auth = {
        "username": "admin",
        "password": "password123"
    }
    #making post req.
    response_data = requests.post(url=full_url, headers=headers, json=json_payload_auth)
    print(response_data)

    #verify the response
    assert response_data.status_code == 200
    response_data_json = response_data.json()
    token = response_data_json["token"]
    print(token)
    assert type(token) == str
    assert len(token) > 0
    return token

#define global fun. for payload to load the data for req.
def get_booking_id():
    base_path = "/booking"
    full_url = base_url + base_path
    print(full_url)
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
    #making req.
    response_data = requests.post(url=full_url, headers=headers, json=json_payload)
    response_data_json = response_data.json()
    booking_id = response_data_json["bookingid"]
    return booking_id

#Create payload
def test_put_request():
    token = get_token()
    bookingid = get_booking_id()
    print(token)
    print(bookingid)
    base_path = "/booking/" + str(bookingid)
    full_url_put = base_url + base_path
    cookie = "token=" + token

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie

    }

    json_payload = {
        "firstname": "Nishita",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }


    response = requests.put(url=full_url_put, headers=headers, json=json_payload)
    assert response.status_code == 200
    assert response.json()["firstname"] == "Nishita"


def test_delete():
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = get_booking_id()
    DELETE_URL = URL + str(booking_id)
    cookie_value = "token=" + get_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }
    response = requests.delete(url=DELETE_URL, headers=headers)
    assert response.status_code == 201


