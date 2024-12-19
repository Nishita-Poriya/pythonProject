def add_before_ui_after_ui(func):

    def wrapper():
        print("Before the running Ui TC")
        print("start the browser")
        func()
        print("Ending the running TC ")
        print("Quit browser")
    return wrapper()

@add_before_ui_after_ui
def test_ui():
    print(">>Test the UI")

