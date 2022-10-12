# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 17:06:48 2021
Assignment 6
@author: Christopher
"""


class ToDo: #defines the class ToDo
    def __init__(self, title, description, iscompleted): 
        self.Title = title
        self.Description = description
        self.IsCompleted = iscompleted

    def MarkComplete(self): #A fucntion to mark an instance of the class ToDo as completed.
        self.IsCompleted = True
        
    def toString(self): #A function to speed the arranging of class information for quick printing.
        return self.Title + " -- " + self.Description + "--" + str(self.IsCompleted)

ToDoList = [ToDo("Example", "Bogus To Do intended solely for demonstrating the program.", False)] #Create a list. In a real program, this would be empty but I incorporated an example To Do to facilitate testing the program.
choice = 0 #sets the choice at 0, which means the program will enter the loop, but not enter any of the indented ifs or  elifs

while choice >= 0: #starts while loop and lists a bunch of choices.
    print("Main Menu -- What do you want to do with your To Do list?")
    print("1. See all of your To Do's.")
    print("2. See outstanding To Do's.")
    print("3. Add a new To Do.")
    print("4. Edit an existing To Do.")
    print("5. Remove an existing To Do.")
    print("6. Mark a To Do as complete.")
    print("7. Exit Program. ")

    choice = int(input()) #accepts a new choice.

    if(choice == 1): #Starts code for choice 1. Will show all To Do's.
        print("Here is your To Do List.")
        counter = 1
        for tasks in ToDoList:
            print(str(counter) + ". " + tasks.toString()) #I added the counter to help identify each instance. I felt this was neccessary for future choices.
            counter +=1
        print("")
        print("Press 'enter' to return to Main Menu.")
        input()

    elif(choice == 2):
        outstanding = []
        for x in ToDoList:
            if x.IsCompleted != True:
                outstanding.append(x)
            else:
                break
                
        print("Here are your outstanding To Do's.") #needs work. Doesn't filter properly
        for tasks in outstanding:
            counter = 1
            print(str(counter) + ". " + tasks.toString())
            print()
            
        print("Press 'enter' to return to Main Menu.")
        input()
        
    elif(choice == 3): #Choice 3 creates a new instance of To Do.
        title = input("Enter a name for this To Do. \nName: ")
        description = input("Please enter a description of this To Do. \nDescription: ")
        iscompleted = False #Default is False, indicating they aren't completed. I see no reason to add a completed To Do so I left this option out.
        task = ToDo(title, description, iscompleted) #creates a new object of class ToDo
        ToDoList.append(task) #appends this object to the To Do List (called ToDoList)
        
    elif(choice == 4): #Choice for allows one to edit a To Do
        choice_edit = 0 #used to select which part of the instance to edit.
        index = int(input("Which To Do would you like to edit? \n"))
        while choice_edit >= 0:
            ToDo_edit = ToDoList[index-1]
            print("Edit Menu -- Which attribute do you want to edit?")
            print("1. Title ")
            print("2. Description ")
            print("3. Completion Status ")
            print("4. Exit to Main Menu ") #This menu will keep appearing until choice 4 is selected.
        
            choice_edit = int(input())
            
            if(choice_edit == 1):
                ToDo_edit.Title = input("Please enter a new title. \n")
            elif(choice_edit == 2):
                ToDo_edit.Description = input("Please enter a new description. \n")
            elif(choice_edit == 3):
                ToDo_edit.IsCompleted = input("Plese enter 'True' to indicate it is completed or 'False' to indicate it is outstanding. \n")
            elif(choice_edit == 4):
                choice_edit = -1
            else:
                print("Please choose a valid option. ")
                print("Press 'enter' continue.") #I just added this so the menu doesn't print right away, which would obscure the warning message above.
                input()
                

    elif(choice == 5):
        index = int(input("Enter the number of the To Do you want to delete or enter 0 to return to the Main Menu. \n"))
        if (index > 0):
            ToDo_remove = ToDoList[index-1]
            print("Are you sure you want to remove '" + str(ToDo_remove.Title) + "'?")
            print("Enter 'Y' or 'N'")
            user_input = input()
            if (user_input == 'Y'):
                del ToDoList[index-1]
            elif (user_input == 'N'):
                choice = 0
            else:
                print("Please enter a valid response.")
        elif (index == 0):
            choice = 0
        else:
            print("Please enter a valid response.")
        
        
    elif(choice == 6): #Choice 6 updates a To Do to completed.
        index = int(input("Enter the number of the To Do would you like to mark as completed, or enter 0 to return to the Main Menu?\n")) #Establishes which instance should be updated.
        ToDoList[index-1].MarkComplete() #Updates to completed. Uses a method I defined for the class.

    elif(choice == 7): #Choice 7 exits the program.
        choice = -1 #Setting choice to -1 will pull the program out of the while loop.
        print("Goodbye! Don't forget to work on some of your To Do list!") #Always end with a sassy message.
        
#The next step would be to write the ToDo to a file, otherwise the users ToDo list would dissappear whenever they exited the program
#Another line could be used to read the ToDo list from the file.
        
        
        