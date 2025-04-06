import pytest
@pytest.fixture()
def is_married_before_run():
    return True

def test_update(is_married_before_run):
    assert is_married_before_run== False

    #here its running update method and it will call is_married fun. which returns true ,
    #if its returning true ==true then its passed otherwise fails
