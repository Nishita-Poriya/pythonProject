def add_security(func): #driveing_scooty called

    def wrapper():
        print("1.Before the function is called")
        print("2.Add Helmet,Dashcash,gloves,knee guards,License")
        func() #diving_scooty is called
        print("3.After the function is called")
        print("4.Secure Driving,Level all the items")
        print("-------Decorator are used to generate logs and reports-------------------------------------")

    return wrapper()

@add_security
def drive_ola_scooter():
    print("ola")


@add_security
def driving_scooty():
    print("Normal Function")
    print("I am driving a scooty!")
