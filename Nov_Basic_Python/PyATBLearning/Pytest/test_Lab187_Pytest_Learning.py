import pytest
def method1():
    print("Hello world")

@pytest.mark.smoke
def test_method2():
    print("test1")
    assert 1-1 == 0

@pytest.mark.regression
def test_method3():
    print("test 2")
    assert 1+1 == 2