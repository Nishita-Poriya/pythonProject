#web Automation -selenium
#page -You are going automate

class VWOLoginPage:

    def __init__(self,email_args,password_arg):
        self.email=email_args
        self.password=password_arg

    def login_confirm(self):
        if self.email=="nishita@gmail.com" and self.password=="Pass123":
            print("Allowed,Login Success")
        else:
            print("Login Filed")


# email = # Read from test data - Excel,CSV or Env file
# password = #Read from test data -Excel.CSV or Env file

# vwo_obj = VWOLoginPage(email, password)
# vwo_obj.login_confirm()

pramod = VWOLoginPage("nishita@gmail.com", "Pass123")
pramod.login_confirm()