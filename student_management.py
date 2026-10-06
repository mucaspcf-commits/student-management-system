# Student Management System
# Create an empty list to store all student records
# Each student record will contain the student name and grade
list_of_students = []
#Set up a Boolean variable to control the main loop
#The System continues executing while this variable is True
system_running = True
# Initiate the program's main loop
# This loop keeps presenting the menu until the user chooses option 5
while system_running:
    print() #add a empty line before de display many
    print("   Student Managment System   ") #Print the title "   Student Managment System   "
    #Print and show to the user all options avaible to select
    print("1)Add Student")#print
    print("2)View students")#print
    print("3)Update student")#print
    print("4)Remove Student")#print
    print("5)Exit")#print
    #Ask to the user to enter an option from main manu
    #strip() removes extra spaces from both sides
    option = input("Choose one of the fallowing options: ").strip()
    #Test  if the user typed something different than a number
    if option.isdigit() == False: # Confirm that the user typed only digits
        print("Select one valid option from the list ") #print
    elif option == "1": #verify if option 1 was selected to record student
        name_student = input("Student name:").strip() #strip() removes extra spaces from both sides
        if name_student == "":#verify if option is empty
            print("Type the Student name , name can not be empty") #print
        else:
            duplicate = False # Set up Boolean flag to confirm if student record exists
            for student_record in list_of_students:
                # Compare the student name saved with name typed by the user
                if student_record[0].lower() == name_student.lower(): #allows names like "Alex" and "ALEX" to be treated as the same.
                    duplicate = True #Change to true because the same name was found
                    break #stop checking because match has been found
            if duplicate == True:#check duplicate name
                print("Student is already recorded in the list") #print
            else:
                grade_student = input("Student Grade (0 to 100):").strip() # Ask for grade, The grade must be between 0 and 100
                if grade_student.isdigit() == False:
                    print("The student’s grade can not have decimals.") #Check whether the entered grade contains only digits. This prevents text or other float values from being accepted.
                else:
                    grade_student = int(grade_student) #convert string to integer
                    if grade_student < 0 or grade_student > 100: #Check if the grade is outside the valid range of 0 to 100
                        print("Enter a grade from 0 to 100..")
                    else:
                        #Save the new student information in the student list.
                        list_of_students.append([name_student, grade_student]) #Each student record is stored as a two-item list.Name in name_student, and grade in grade_student
                        #Identify the grade classification from the student’s score.
                        if grade_student < 50: #result of 50 is categorized as Fail
                            grade_category = "F - Fail"
                        elif grade_student < 65: # Results from 50 to 64 are categorised as Pass
                            grade_category = "P - Pass"
                        elif grade_student < 75: # Results from 65 to 74 are classified as Credit
                            grade_category = "C - Credit"
                        elif grade_student < 85: # Results from 75 to 84 are classified as Distinction
                            grade_category = "D - Distinction"
                        else:
                            grade_category = "HD - High Distinction" # Results  from 85 to 100 are classified as High Distinction
                        print() #add a empty line
                        print("Name:", name_student) #Print Student Name
                        print("Grade:", grade_student) #Print Student Grade
                        print("Category:", grade_category) #Print Student Category
    elif option == "2": #Verify if option 2 was selected to view the student records
        if len(list_of_students) == 0:
            print("There are no student records available.")#print
        else:
            print("")#add a empty line
            print("Student Records")#print
            print("")#add a empty line
            for student_record in list_of_students:#check each student recorded
                name_student = student_record[0]#Get the student name stored in position 0 of the student record
                grade_student = student_record[1] #Get the student grade stored in position 1 of the student record
                if grade_student < 50:#result of 50 is categorized as Fail
                    grade_category = "F - Fail"
                elif grade_student < 65:# Results from 50 to 64 are categorised as Pass
                    grade_category = "P - Pass"
                elif grade_student < 75:# Results from 65 to 74 are classified as Credit
                    grade_category = "C - Credit"
                elif grade_student < 85:# Results from 75 to 84 are classified as Distinction
                    grade_category = "D - Distinction"
                else:# Results  from 85 to 100 are classified as High Distinction
                    grade_category = "HD - High Distinction"
                print("Name:", name_student) #show student name
                print("Grade:", grade_student)#show student grade
                print("Category:", grade_category)#show student grade category
                print("")#print
    elif option == "3": #verify if option 3 was selected to  update an existing student
        if len(list_of_students) == 0: # len returns the number of items in the list.
            print("There are no student records available.")#print
        else:
            old_name = input("Enter the name of the student to update:").strip() #Instruct the user to enter the student’s registered name.This name will help locate the student record.
            student_found = False # Set up Boolean flag to confirm if student is found
            for student_record in list_of_students: #Scan each student record to find the requested student.
                if student_record[0].lower() == old_name.lower(): #Compare the stored name with the user typed and lower() ignores uppercase and lowercase differences.
                    student_found = True #Change to true because the same name was found
                    name_updated = input("Enter new name: ").strip() # type new name
                    grade_upgrade = input("Enter new grade: ").strip() # type new grade
                    if name_updated == "": # Verify if new name was left blank
                        print("A student name is required..") #print
                    elif grade_upgrade.isdigit() == False: #Verify if updated grade contains only digits.
                        print(" enter a valid number..") #print
                    else:
                        grade_upgrade = int(grade_upgrade) # convert text into an integer
                        if grade_upgrade >= 0 and grade_upgrade <= 100: # Check that the grade is within the permitted values.
                            student_record[0] = name_updated  # Replace the old student name with the new name
                            student_record[1] = grade_upgrade # Replace the old student grade with the new grade
                            print("Student record updated successfully") # Print the Confirmation
                        else:
                            print("Invalid grade.") #print message that the new grade is out of range.
                    break #stop checking because match has been found
            if student_found == False: # Confirmation that the requested student was not found.
                print("Student not found.") #print
    elif option == "4": #verify if option 4 was selected to  remove an existing student
        if len(list_of_students) == 0: # len returns the number of items in the list.Confirm that at least one student record exists before deletion.
            print("There are no student records available.")#print
        else:
            name_remove = input("Enter student name to remove: ").strip() # request to the user the name of the student to remove
            student_found = False #Change to true because the same name was found
            for student_record in list_of_students: #Scan each student record to find the requested student.
                if student_record[0].lower() == name_remove.lower(): #Compare the stored name with the user typed and lower() ignores uppercase and lowercase differences.
                    list_of_students.remove(student_record) # Remove the student record from the list
                    student_found = True # student was found and removed
                    print("Student removed.") #Confirmation of the removal to the user
                    break #stop checking because match has been found
            if student_found == False:#check if  the student cannot be found.
                print("Student not found.") #message when the student cannot be found.
    elif option == "5": #verify if option 5 to exit the system
        print("Program closed.") #Display a message before exiting the program.
        system_running = False #Change the loop variable to False, which ends the main loop.
    else: #Respond to any invalid numerical menu option
        print("Invalid menu option.") #print