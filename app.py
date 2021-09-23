"""This is the central program that invites all modules"""
from cours import Courses
from trainer import Trainers
from student import Students
from assignment import Assignments


def main():
    """Function main and all running project"""
    stop = ''
    while stop != 'x':
        # List for courses, students, trainers, assignments
        lists = []

        # Courses
        crs = Courses.course()
        print(crs)

        # Trainers
        trs = Trainers.trainer()
        print(trs)

        # Students
        std = Students.student()
        print(std)

        # Assignments
        asg = Assignments.assignment()
        print(asg)

        # Stoping or Continue Program
        print('*' * 30)     # Separation of information
        stop = input("Continue: Enter, Exit: x : ")

        # Append list courses, students, trainers, assignments
        listas = (crs, trs, std, asg)
        for lista in listas:
            lists.append(lista)

        # List all the above items
        print('*' * 30)     # Separation of information
        print(lists)        # output list courses, students, trainers, assignments


# Run Program
if __name__ == '__main__':
    main()
