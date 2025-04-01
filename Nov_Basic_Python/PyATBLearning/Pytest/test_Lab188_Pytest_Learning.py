import pytest
import allure

@allure.title("Verify the create booking , with valid data is working ")
@allure.description("This T.C for check the positive create booking")
@pytest.mark.positive
def test_create_booking_positive():
    print("test1")
    assert 1-1==2

@allure.title("Verify that create booking with invalid data is working")
@allure.description("This test case check for negative create booking")


@pytest.mark.negative
def test_create_booking_negative1():
    print("test2 negative 1")
    assert 1+1==2

@allure.title("Verify that create booking, with invalid data is working")
@allure.description("This Testcase check for the negative  create booking")
@pytest.mark.negative
def test_create_booking_negative2():
    print("test2 negative 2")
    assert 1+1==2


