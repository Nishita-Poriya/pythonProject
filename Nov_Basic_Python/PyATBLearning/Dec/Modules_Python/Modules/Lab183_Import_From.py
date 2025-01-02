from browserPackage.OpenBrowser import start_browser
from browserPackage.CloseBrowser import stop_browser


def TestCase():
    start_browser()
    print("Hello running TC")
    stop_browser()

obj_tc=TestCase()
obj_tc.test_Case()