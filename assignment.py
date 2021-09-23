from cours import Courses
from student import Students


class Assignments(Students, Courses):
    def __init__(self, mylists, title, descp, date_sub, mark_sub, oral_mark):
        self.mylists = mylists
        self.title = title
        self.descp = descp
        self.date_sub = date_sub
        self.mark_sub = mark_sub
        self.oral_mark = oral_mark


    @classmethod
    def assignment(cls):
        print('*' * 30)         # Separation of information
        print('Assignments')    # Title
        mylists = []

        """
        Checks that the string have been completed
        otherwise to print a message
        """
        while True:
            try:
                # Fill in the details courses in input
                title = input("Give your title: ")
                descp = input("Give your description: ")
                date_sub = input("Give your date of submission: ")
                mark_sub = float(input("Give your mark for the submitted code: "))
                oral_mark = float(input("Give your mark for the oral mark: "))

                """
                Adds his two course numbers and then divides
                them and print by You passed or Cuts
                """
                grades = mark_sub + oral_mark
                total = grades // 2
                sum_total = ['You passed' if total > 50 else 'Cuts']
                
                """
                Append list assignment
                the items in tuples enter in for
                loop and list append
                """
                items = (title, descp, date_sub, mark_sub, oral_mark, total, sum_total)
                for item in items:
                    mylists.append(item)
                return mylists
            except ValueError:
                print("Oops! Sorry, enter all the details on the form. Try again...")
