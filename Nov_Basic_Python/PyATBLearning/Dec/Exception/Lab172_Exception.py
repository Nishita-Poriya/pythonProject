class XYZ:
    def f1(self):
        try:
            a=int(input("Enter a number\n"))
        except Exception as e:
            print("Enter int only value of a")
        else:
            print(a)

        finally:
            print("Final:Anyhow i will be printed")

x_obj_ref=XYZ()
x_obj_ref.f1()