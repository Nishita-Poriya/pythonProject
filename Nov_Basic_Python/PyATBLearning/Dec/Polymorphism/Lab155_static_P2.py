class ExcelReader:

    @staticmethod
    def read_from_excel():
        print("Reading from Excel")

class MYSQLDBConnection:

    @staticmethod
    def readyMYSQLFile():
        print("Reading from MYSQL")

class TC1:
    static_var =10

    @staticmethod
    def testcase():
        MYSQLDBConnection.readyMYSQLFile()
        ExcelReader.read_from_excel()
        print(TC1.static_var)  # Shared among all instances of the class

TC1.testcase()