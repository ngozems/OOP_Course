class Student:

    def readStudentDetails(self):
        Name = input("Enter studentname:")
        RollNo = input("Enter rollno:")

        # code to enter subjects
        n = 3
        print("Enter three subjects:")
        subjectList = []
        for i in range(0, 3):
            subject = input()
            subjectList.append(subject)

        # code to enter marks
        marks = []
        for subject in subjectList:
            mark = int(input("Enter the mark of " + subject + ":"))
            marks.append(mark)

        self.__Name = Name
        self.__RollNo = RollNo
        self.__Subjects = subjectList
        self.__Marks = marks

        self.__Total = len(self.__Marks)
        self.__Average = round(sum(self.__Marks) / self.__Total, 2)

        self.__Grade = self.computeGrade()

    def computeGrade(self):
        grade_map = {50: "F", 60: "D", 75: "C", 85: "B", 101: "A"}
        for reference_grade in grade_map:
            if self.__Average < reference_grade:
                grade = grade_map[reference_grade]
                break
        return grade

    def displayStudentDetails(self):
        print("Name is " + self.__Name)
        print("Rollno is " + str(self.__RollNo))
        print("Subjects are: " + ", ".join(self.__Subjects))
        print("Marks are: " + ", ".join([str(mark) for mark in self.__Marks]))
        print("Average mark is: " + str(self.__Average))
        print("Grade is: " + self.__Grade)


student = Student()
student.readStudentDetails()
student.displayStudentDetails()
