class Courses:
    def __init__(self, mylists, title, lang, descp, types):
        self.mylists = mylists
        self.title = title
        self.lang = lang
        self.descp = descp
        self.types = types


    @classmethod
    def course(cls):
        print('Courses')   # Title
        mylists = []

        """
        Checks that the string have been
        completed otherwise to print a message
        """
        while True:
            # Fill in the details students in input
            title = input("Give your title: ")
            lang = input("Give your language: ")
            descp = input("Give your description: ")
            types = input("Give your full or part time: ")

            """
            when the data is blank it will do try again
            for to fill in mandatory and when the data
            is completed go to else and do append to the list
            """
            if title == '' or lang == '' or descp == '' or types == '':
                print('Try again...')
            else:
                """
                Append list courses the items in tuples
                enter in for loop and list append
                """
                items = (title, lang, descp, types)
                for item in items:
                    mylists.append(item)
                return mylists
        print('*' * 30)
