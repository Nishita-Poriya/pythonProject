import pytest
import allure
import requests

@allure.title("Verify the GET requests of restful booker")
@allure.description("This testcase check booking 1 and verify the response")
@pytest.mark.positive
def test_get_request_positive():
    url_get = "https://restful-booker.herokuapp.com/booking/1"
    response_data=requests.get(url=url_get)
    assert response_data.status_code==200

@allure.title("Verify Get request with of restful booker with invalid ID")
@allure.description("This TC to check Booking -1 & response ")
@pytest.mark.negative
def test_get_request_negative():
    url_get = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url=url_get)
    assert response_data.status_code == 404
