from cours import Courses


class Students(Courses):
    def __init__(self, mylists, fname, lname, birth, fees):
        self.mylists = mylists
        self.fname = fname
        self.lname = lname
        self.birth = birth
        self.fees = fees


    @classmethod
    def student(cls):
        print('*' * 30)     # Separation of information
        print('Students')   # Title
        mylists = []
        
        """
        Checks that the string have
        been completed otherwise to
        print a message
        """
        while True:
            """
            When the data is blank it will do
            try again for to fill in mandatory

            """
            try:
                fname = input("Give your first name: ")
                lname = input("Give your last name: ")
                birth = input("Give your date of birth: ")
                fees = int(input("Give your tuition fees: "))
                

                """
                Puts the use to choose its doses
                and displays a message for try again,
                if it puts more or less than a limit
                """
                if fees <= 4 or fees >= 20:
                    print('Try again, please from 4 in 20')
                else:
                    """
                    Append list student the items in
                    tuples enter in for loop and list
                    append
                    """
                    items = (fname, lname, birth, fees)
                    for item in items:
                        mylists.append(item)
                    return mylists
            except ValueError:
                print("Oops! Sorry, enter all the details on the form. Try again ...")
