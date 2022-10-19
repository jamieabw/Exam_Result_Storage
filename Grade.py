class Grade:
    def __init__(self, subject, paper_name, grade):
        self.__subject = subject
        self.__paper_name = paper_name
        self.__grade = grade

# getters are used due to private fields being used in the class, only way to access values stored
    def get_subject(self):
        return self.__subject

    def get_paper_name(self):
        return self.__paper_name

    def get_grade(self):
        return self.__grade