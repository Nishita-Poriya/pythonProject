
#use of super() > to call the parent method for method overloading
class OldBrowser:

    def start_browser(self):
        print("IE browser is starting")

    def stop_browser(self):
        print("IE browser is closing")


class Chrome(OldBrowser):

    def start_browser(self):
        super().start_browser() #called parent start browser also
        print("Better Chrome browser is starting ....")
        print("-----------")

    def stop_browser(self):
       #super().stop_browser()
       print("better chrome browser is stopping ...")

    pass

object_ref=Chrome()
object_ref.start_browser()
object_ref.stop_browser()