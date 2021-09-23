from cours import Courses


class Trainers(Courses):
    def __init__(self, mylists, fname, lname, subj):
        self.mylists = mylists
        self.fname = fname
        self.lname = lname
        self.subj = subj


    @classmethod
    def trainer(cls):
        print('*' * 30)     # Separation of information
        print('Trainers')   # Title
        mylists = []

        """
        Checks that the string have been
        completed otherwise to print a
        message
        """
        while True:
            # Fill in the details students in input
            fname = input("Give your first name: ")
            lname = input("Give your last name: ")
            subj = input("Give your subject: ")


            """
            When the data is blank it will do try
            again for to fill in mandatory and
            when the data is completed go to
            else and do append to the list
            """
            if fname == '' or lname == '' or subj == '':
                print('Try again...')
            else:
                """
                Append list courses the items in
                tuples enter in for loop and list
                append
                """
                items = (fname, lname, subj)
                for item in items:
                    mylists.append(item)
                return mylists
        print('*' * 30)     # Separation of information

