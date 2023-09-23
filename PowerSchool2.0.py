# from here (excluding any methods that specifically have Harsh's name on it) -->
class Student():

    def __init__(self, provName, provID, provSchedule = [], provGrades = [], provGoalSet = [], provtestSec = [], provHQASec = [], provFinalSec = []):
        self.name = provName
        self.ID = provID
        self.schedule = provSchedule
        self.grades = provGrades
        self.goalSet = provGoalSet
        self.testSec = provtestSec
        self.HQASec = provHQASec
        self.finalSec = provFinalSec

    def ovrAve(self):
       print("Your overall average between all courses is " + str(sum(self.grades)/len(self.grades)) + ".") 
   
    def scheduleView(self):#Harsh
        for i in range(len(self.schedule)):
            print("Period " + str(i+1) + ": " + self.schedule[i])
       
    def setGoals(self):
        givenName = input("Please enter you name: ")
        givenID = input("Please enter your ID:  ")
        settingGoal = True
        if givenName == self.name and givenID == self.ID:
            while settingGoal == True:
                provCourse = input("Please enter the course you wish to set a goal for: ")
                for i in range(len(self.schedule)):
                    if provCourse == self.schedule[i]:
                        print("The current mark for " + self.schedule[i] + " is " + str(self.grades[i]) + "." )
                        goal = int(input("Please enter the goal you wish to set for this course: "))
                        self.goalSet[i] = goal
                        print("Your current goal for this course is " + str(self.goalSet[i]) + ".")
                        choiceAnotherGoal = input("Would you like to set a goal for another course? (Please type either 'Yes' or 'No'): ")
                        if choiceAnotherGoal == "No":
                            settingGoal = False
                            break 
        else: 
            print("You're given name and ID do not match. ")
            
    def individualCourse(self):#Harsh
        lookingCourse = True
        while lookingCourse == True:
            view = input("Which course would you like an in depth view of? ")
            for i in range(len(self.schedule)):
                if view == self.schedule[i]:
                    print("Your current mark for this course is " + str(self.grades[i]) + ".")
                    print("Your mark for the Unit Tests section of this grade is " + str(self.testSec[i]) + ". This section is weighted at 50% of your overall course mark.")
                    print("Your mark for the Homework/Quizzes/Assignments section of this grade is " + str(self.HQASec[i]) + ". This section is weighted at 20% of your overall course mark.")
                    if self.finalSec[i] == -1:
                        print("You currently have no grade for the Final Exam section because you have not written a final exam for this course. This section is weighted at 30% of your overall course mark.")
                    else:
                        print("Your mark for the Final Exam section of this grade is " + str(self.finalSec[i]) + ". This section is weighted at 30% of your overall course mark.")
                    choiceAnotherView = input("Would you like to see another course's in depth view? (Please type either 'Yes' or 'No'): ")
                    if choiceAnotherView == "No":
                        lookingCourse = False
                        break
        
    
    def getStudentID(self):
        return self.ID
    
    def getStudentName(self):
        return self.name
    
    def getSchedule(self):
        return self.schedule
    
    def getTestSec(self, i):
        return self.testSec[i]
    
    def getHQASec(self, i):
        return self.HQASec[i]
    
    def getFinalSec(self, i):
        return self.finalSec[i]
    
    def getAverage(self, i):
        return self.grades[i]
    
    def AddCourse(self, newCourse):
        self.schedule.append(newCourse)
        
    def setFinal(self, course, mark):
        self.finalSec[course] = mark
        
    def newOvrAve(self, i):
        overall = (self.testSec[i]*0.5) + (self.HQASec[i]*0.2) + (self.finalSec[i]*0.3)
        self.grades[i] = overall
        return overall
    
    
if __name__ == "__main__":
    
    student1 = Student("Abdul", "1111", ["Math","English","Science","Social"], [80,90,80,90],[80,90,80,90],[72,86,74,90],[100,100,95,90],[-1,-1,-1,-1])
    student2 = Student("Nastia", "2222", ["Math","English","Science","Social"], [50,80,90,85],[50,80,90,85],[46,90,100,85],[60,55,30,85],[-1,-1,-1,-1])
    student3 = Student("Lamelo", "3333", ["Math","English","Science","Social"], [100,95,95,98],[100,95,95,98],[100,95,95,98],[100,95,95,98],[-1,-1,-1,-1])
    student4 = Student("Tiffany", "4444", ["Math","English","Science","Social"], [80,85,95,90],[80,85,100,89],[80,85,95,90],[80,85,95,90],[-1,-1,-1,-1])
    student5 = Student("Kofo", "5555", ["Math","English","Science","Social"], [100,100,100,100],[100,100,100,100],[100,100,100,100],[100,100,100,100],[-1,-1,-1,-1])

    Students = [student1, student2, student3, student4, student5]
    
    def teacherAddCourse():
        nameCourse = input("What is the name of the course you would like to add?: ")
        for students in Students:
            students.AddCourse(nameCourse)
            
    def updateMarks():
        courseTaught = input("What course do you teach? ")
        for students in Students:
            for i in range(len(students.getSchedule())):
                if courseTaught == students.getSchedule()[i]:
                    finalExam = int(input("What mark did " + students.getStudentName() + " get on the Final Exam?: "))
                    students.setFinal(i, finalExam)
                    print(students.getStudentName() + "'s new overall mark is " + str(students.newOvrAve(i)) + ".")


    def classProgress():
        viewCourseTaught = input("What course do you teach? ")
        for students in Students:
            for i in range(len(students.getSchedule())):
                if viewCourseTaught == students.getSchedule()[i]:
                    print("Name: " + students.getStudentName() + " /Test Section Average: " + str(students.getTestSec(i)) + " /Homework/Quizzes/Assignments Section: " + str(students.getHQASec(i)) + " /Final Exam Section Average: " + str(students.getFinalSec(i)) + " /Overall Average: " + str(students.getAverage(i)))

    def teacherStudentView():#Harsh
        nameOfStudent = input("What is the name of the student you wish to view?: ")
        for students in Students:
            if nameOfStudent == students.getStudentName():
                course = input("What course do you teach this student?: ")
                for i in range(len(students.getSchedule())):
                    if course == students.getSchedule()[i]:
                        print("Overall Grade = " + str(students.getAverage(i)) + "\nUnit Test Section (50% of Overall Grade) = " + str(students.getTestSec(i)) + "\nHomework/Quizzes/Assignments Section (20% of Overall Grade) = " + str(students.getHQASec(i)) + "\nFinal Exam Section (30% of Overall Grade) (If output = '-1', the Final Exam has not been written yet) = " + str(students.getFinalSec(i)))
    
    def sectionalClassAverage():
        sectionClass = input("What course do you teach? ")
        sectionChoice = input("What section of the course would you like a class average of? ('Unit Test', 'HQA Section', 'Final Exam', 'Overall Average'):  ")
        for students in Students:
            for i in range(len(students.getSchedule())):
                if sectionClass == students.getSchedule()[i]:
                    if sectionChoice == "Unit Test":
                        sum1 = 0
                        for students in Students:
                            sum1 += students.getTestSec(i)
                        utsa = sum1/len(Students)
                    elif sectionChoice == "HQA Section":
                        sum2 = 0
                        for students in Students:
                            sum2 += students.getHQASec(i)
                        hqasa = sum2/len(Students)
                    elif sectionChoice == "Final Exam":
                        sum3 = 0
                        for students in Students:
                            sum3 += students.getFinalSec(i)
                        fasa = sum3/len(Students)
                    elif sectionChoice == "Overall Average":
                        sum4 = 0
                        for students in Students:
                            sum4 += students.getAverage(i)
                        oasa = sum4/len(Students)
                    else:
                        print("You have entered an invalid option. Please try again.")
        if sectionChoice == "Unit Test":
            print("Unit Test section class average: " + str(utsa))
        elif sectionChoice == "HQA Section":
            print("Homework/Quiz/Assignment secion class average: " + str(hqasa))
        elif sectionChoice == "Final Exam":
            print("Final exam secion class average: " + str(fasa))
        elif sectionChoice == "Overall Average":
            print("Overall Average secion class average: " + str(oasa))
        else:
            print("You have entered an invalid option. Please try again.")
# to here --> = Kameel                   
    
    print("Welcome to Powerschool 2.0") #from here -->
    print("")
    
    usernameFile = open("pythonUsernames.txt", "r")
    passwordFile = open("pythonPasswords.txt", "r")

    username = usernameFile.readlines()
    password = passwordFile.readlines()
    usernameFile.close()
    passwordFile.close()
    
    usernameFile = open("pythonUsernames.txt", "a")
    passwordFile = open("pythonPasswords.txt", "a")

    signIn = 0
    while signIn == 0:
        account = input('Would you like to LOGIN or CREATE an account?: ')
        if account == "LOGIN":
            signIn = 1
        elif account == "CREATE":
            signIn = 2
        else: 
            print("The input is invalid. Please try again.")

    
    while signIn == 2:
        print("")
        newUser = input("Enter your new username (4 digit ID): ")
        newPass = input("Enter your new password (3 digit number): ")
        usernameFile.write(newUser + "\n")
        passwordFile.write(newPass + "\n") 
        usernameFile.close()
        passwordFile.close()
        print("")
        print("Your username and password have been saved please re-run the program to sign in.")
        break
        
    while signIn == 1:
        with open('pythonUsernames.txt') as a:
            teacher_user = a.readline(7)
        with open('pythonPasswords.txt') as b:
            teacher_pass = b.readline(7)
        currentUser = input("Enter your Username: ")
        currentPass = input("Enter your Password: ") 
        while currentUser == teacher_user and currentPass == teacher_pass:
            print("")
            print("You are now logged in as a teacher!")
            print("We have the following options.")
            print("1. Create a Course")
            print("2. Update Marks")
            print("3. View Class Scores")
            print("4. View Individual Student Scores")
            print("5. Sectional Class Averages")
            print("6. Exit")
            teachChoice = int(input("Which option would you like to explore?: "))
            if teachChoice == 1:
                print("")
                teacherAddCourse()
            elif teachChoice == 2:
                print("")
                updateMarks()
            elif teachChoice == 3:
                print("")
                classProgress()
            elif teachChoice == 4:
                print("")
                teacherStudentView()
            elif teachChoice == 5:
                print("")
                sectionalClassAverage()
            elif teachChoice == 6:
                print("")
                print("Thank you for Using Powerschool 2.0! Bye Bye!")
                break
            else:
                print("")
                print("You have entered an invalid option. Please try again. ")

        else:
            for i in range (len(username)):
                if username[i].strip("\n") != currentUser and password[i].strip("\n") != currentPass:
                    if(i+1 >= len(username)):
                        print("")
                        print("Your username or password are incorrect. Please create a new account or try again.")
                else:
                    for students in Students:
                        while currentUser == students.getStudentID(): 
                            print("")
                            print("You are now logged in " + students.getStudentName() + "!")
                            print("We have the following options.")
                            print("1. View Overall Average")
                            print("2. View Student Schedule")
                            print("3. Set Academic Goals")
                            print("4. In Depth Course View")
                            print("5. Exit")
                            choice = int(input("What option would you like to explore?: "))
                            if choice == 1:
                                print("")
                                students.ovrAve()
                            elif choice == 2:
                                print("")
                                students.scheduleView()
                            elif choice == 3:
                                print("")
                                students.setGoals()
                            elif choice == 4:
                                print("")
                                students.individualCourse()
                            elif choice == 5:
                                print("")
                                print("Thank you for Using Powerschool 2.0! Bye Bye!")
                                break
                            elif choice == " ": 
                                print("")
                                print("You have entered an invalid option. Please try again. ")
                            else:
                                print("")
                                print("You have entered an invalid option. Please try again. ")
                    break 

# to here --> = Harsh
