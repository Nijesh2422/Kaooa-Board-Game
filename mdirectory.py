import csv
from prettytable import PrettyTable

class Entry:
    Marks_List = []
    def __init__(self,first_name,last_name,roll_number,course_name,semester,exam_type,total_marks,scored_marks):
        self.first_name = first_name
        self.last_name = last_name
        self.roll_number = roll_number
        self.course_name = course_name
        self.semester = semester
        self.exam_type = exam_type
        self.total_marks = total_marks
        self.scored_marks = scored_marks
        Entry.Marks_List.append(self)   

    def DeleteClass(roll_number,course_name,semester,exam_type):
        for entry in Entry.Marks_List:
            if entry.roll_number == roll_number and entry.course_name == course_name and entry.semester == semester and entry.exam_type == exam_type :
                Entry.Marks_List.remove(entry)
                print("Entry Deleted")
                return
        print("Entry Not Found")
        return
    
    def UpdateClass(roll_number,course_name,semester,exam_type,new_scored_marks):
        for entry in Entry.Marks_List:
            if entry.roll_number == roll_number and entry.course_name == course_name and entry.semester == semester and entry.exam_type == exam_type :
                entry.scored_marks = new_scored_marks
                print("Entry Updated")
                return
        print("Entry Not Found")
        return
    
    def DisplayTable():
        table = PrettyTable()
        table.field_names = ["First Name","Last Name","Roll Number","Course Name","Semester","Exam Type","Total Marks","Scored Marks"]
        for entry in Entry.Marks_List:
            table.add_row([entry.first_name,entry.last_name,entry.roll_number,entry.course_name,entry.semester,entry.exam_type,entry.total_marks,entry.scored_marks])
        print(table)

    def CsvReader(name_of_file):
        try:
            given_file = open(name_of_file,'r',newline='')
            given_file.close()
        except:
            print("File not found")
            return
        with open(name_of_file,'r',newline='') as given_file:
            csv_reader = csv.reader(given_file)
            next(csv_reader)
            for row in csv_reader:
                first_name = row[0]
                last_name = row[1]
                roll_number = row[2]
                course_name = row[3]
                semester = row[4]
                exam_type = row[5]
                total_marks = row[6]
                scored_marks = row[7]
                flag = 0
                for i in Entry.Marks_List:
                    if roll_number == i.roll_number and course_name == i.course_name and semester == i.semester and exam_type == i.exam_type : 
                        flag += 1
                        break
                if flag == 0:
                    Jobtect = Entry(first_name,last_name,roll_number,course_name,semester,exam_type,total_marks,scored_marks)
        print("CSV file loaded into the directory")

    def SearchFilt(OptionTwo,Value,Attribute):
        table = PrettyTable()
        table.field_names = ["First Name","Last Name","Roll Number","Course Name","Semester","Exam Type","Total Marks","Scored Marks"]
        for entry in Entry.Marks_List:
            if getattr(entry,Attribute) == Value:
                table.add_row([entry.first_name,entry.last_name,entry.roll_number,entry.course_name,entry.semester,entry.exam_type,entry.total_marks,entry.scored_marks])
        print(table)
        return
    
dicto  = ["First Name","Last Name","Roll Number","Course Name","Exam Type"]
dicto2 = ["first_name","last_name","roll_number","course_name","exam_type"]
while True:
    try:
        Option = int(input("Select one of the option \t\n1 : New Entry\t\n2 : Load from CSV File\t\n3 : Display the Directory\t\n4 : Remove an Entry\t\n5 : Update an Entry\t\n6 : Search\t\n7: Load and Exit!!!!! \n"))
    except:
        print("To select an option enter it's corresponding value (from 1 to 7)",end='\n\n')
        continue
    if Option == 1:
        first_name = input("First Name: ")
        last_name = input("Last Name : ")
        roll_number = input("Roll number : ")
        course_name = input("Course name : ")
        semester = input("Semester : ")
        exam_type = input("Exam Type : ")
        total_marks = input("Total Marks : ")
        scored_marks = input("Scored Marks : ")
        flag = 0
        for i in Entry.Marks_List:
            if roll_number == i.roll_number and course_name == i.course_name and semester == i.semester and exam_type == i.exam_type : 
                flag += 1
                break
        if flag == 0 :    
            Object = Entry(first_name,last_name,roll_number,course_name,semester,exam_type,total_marks,scored_marks)
    if Option == 2:
        name_of_file = input("Name of file : ")
        Entry.CsvReader(name_of_file)
    if Option == 3:
        Entry.DisplayTable()
    if Option == 4:
        roll_number = input("Roll number : ")
        course_name = input("Course name : ")
        semester = input("Semester : ")
        exam_type = input("Exam Type : ")
        Entry.DeleteClass(roll_number,course_name,semester,exam_type)
    if Option == 5:
        roll_number = input("Roll number : ")
        course_name = input("Course name : ")
        semester = input("Semester : ")
        exam_type = input("Exam Type : ")
        new_scored_marks = input("Updated Marks : ")
        Entry.UpdateClass(roll_number,course_name,semester,exam_type,new_scored_marks)
    if Option == 6:
        print("Select the filter:")
        OptionTwo = int(input("1 : First Name\n2 : Last Name\n3 : Roll Number\n4 : Course Name\n5 : Exam Type\n"))
        print()
        Value = input(f"Enter the value of {dicto[OptionTwo-1]} to be searched upon : ")
        Entry.SearchFilt(OptionTwo,Value,dicto2[OptionTwo-1])
    if Option == 7:
        try : 
            aapshan = int(input("Select an Option:\t\n1: Load the data into a csv file\t\n2: Exit without loading\n"))
        except:
            print("To select an option enter it's corresponding value (from 1 to 7)",end='\n\n')
        if aapshan == 1:
            filename = input("Enter the name of csv file to load into: ")
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)  
                writer.writerow(["First Name","Last Name","Roll Number","Course Name","Semester","Exam Type","Total Marks","Scored Marks"])
                for i in Entry.Marks_List:
                    writer.writerow([i.first_name,i.last_name,i.roll_number,i.course_name,i.semester,i.exam_type,i.total_marks,i.scored_marks])
        print("BaiBai\n")
        break

    print()
    print()
