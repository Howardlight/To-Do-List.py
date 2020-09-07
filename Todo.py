#! python3
"""To Do list"""

import sys
import os



# Branch the code out into multiple files IE make it tidy
# Create a nice graphic to display the to do list
# Make the to do list CMD compatible
# Create a __main__
# Factor and improve the code by turning it to functions and classes
# Upgrade the todolist to a dictionnary so that i can contain more info about each task
class notepad():
    def __init__(self):
        ''' the Core functionality of the script, can be modified to load or
            create new notepads'''
    
    # TODO LATER
    # FIRST learn how to append to an already existing todo
    # IE load a notepad then try to implement the class.




### for later ###
# argnumber = len(sys.argv)
# argparsed = str(sys.argv)
# argslengh = len(sys.argv)
# args = sys.argv

def main():

    ExistingTodos = []
    ToDolist = []
    def Startscreen():
        print("Please select an argument. \n 1- add \n 2- remove \n 3- exit \n 4- show \n 5- args")
    number = 1
    print('Welcome to To Do list!')

    # TODO: find a better implementation for this, folderName and subfolders are unused
    for folderName, subfolders, filenames in os.walk("D:/Projects/TodoList Python"): # NOTE: May need to change these 2
        for Todos in filenames:
            numberrelatedtofiledetected = 0
            if Todos.lower().endswith(".txt"):
                ExistingTodos.append(Todos)
                numberrelatedtofiledetected += 1
                displayfiledetected = os.path.join('D:/Projects/TodoList Python', Todos) # Change this later                                                  
                print(f'{numberrelatedtofiledetected}: {displayfiledetected}') # NOTE: May need to change these 2                         
        
        else:
            break #

    print('')
    Loadorcreate = input('Would you like to load a todo list or create a new one? (l/n)')
    while True:
        if Loadorcreate == 'l':
            for file in ExistingTodos:
                print(file)

            while True:
                # TODO: add a gate for when someone inputs a 0
                # TODO: add a gate for when there are no files and user picked load (l)
                selectloadfileinput = int(input('which file would you like to open ?'))  - 1

                if selectloadfileinput > len(ExistingTodos):
                    print('That file does not exist! \n')

                else:
                    loadthisfile = os.path.join('D:/Projects/TodoList Python', str(ExistingTodos[selectloadfileinput]))
                    with open(loadthisfile, 'r') as loadedfile:
                        for line in loadedfile:
                            ToDolist.append(line)
                    break
                break
            break


        elif Loadorcreate == 'n':
            loadthisfile = False
            break 


    Startscreen()
    # TODO: CREATE A CLASS FOR THIS FOR THE LOAD IMPLEMENTATION
    while True:    
        inputtedCommand = input('>> ')


        if inputtedCommand == 'add':
            newTodo = input('Please input your new todo >> ')
            ToDolist.append(newTodo)
            print(f'Added "{newTodo}" to your Todo list!')


        elif inputtedCommand == 'remove':

            if len(ToDolist) <= 0:
                print('Your to do list is empty. \n')

            else:
                while True:

                    while True:
                        try:
                            tododelete = int(input(f"""Please select which todo you want to remove \n{str(ToDolist)} \ntype '0' to cancel \n>> """))
                            break
                        except Exception:
                            print('You can only numbers!')


                    if tododelete == 0:
                        print('Cancelling.. ')
                        print('')
                        Startscreen()
                        break
                
                    
                    elif tododelete:

                        if int(tododelete) > len(ToDolist):
                            print('That todo does not exist!')

                        else:
                            print(f'Deleting {ToDolist[(int(tododelete) - 1)]} from your todo list...')
                            ToDolist.pop(int(int(tododelete) - 1))
                            print('Item Deleted! \n')


                    

        elif inputtedCommand == 'exit':
                print('exitting... \n')
                #####
                # Fixed it Kek
                # TODO: make it so it doesn't overwrite the file, by reading it
                # first then appending to it
                # TODO: make the script load the file
                # TODO: allow the user to choose a script?
                # TODO: allow the user to name the txt? [very easy to implement]

                # Checks if current filename exits.
                Tosavefile = f'Save{number}.txt'
                while os.path.exists(str(Tosavefile)):
                    number += 1
                    Tosavefile = f'Save{number}.txt'

                # Writes to a file
                if loadthisfile:
                    with open(loadthisfile, 'w') as f:
                            f.write('\n'.join([' '.join(i) for i in ToDolist]))
                else: 
                    with open(Tosavefile, 'w') as f:
                        f.write('\n'.join([' '.join(i) for i in ToDolist]))

                break


        elif inputtedCommand == 'show':
            numberoftodos = 0
            # TODO: add a gate for when the list is empty
            for i in range(len(ToDolist)):
                numberoftodos += 1
                print(f"{numberoftodos}- {ToDolist[i]}")


        elif inputtedCommand == 'args':
            print('')
            Startscreen()
        

        # TO BE ADDED #
        else:
            print("I'm sorry, i dont understand... \n")




if __name__ == '__main__':
    main()
#print(" argument number: " + str(argnumber) + " arguments")
#print('arguments detected: ' + argparsed)


#if argslengh <= 1:
    #print('Welcome to To Do list dot py! \n Please select an argument.')

#if argslengh >= 1:
   #rint(sys.argv[1])


# find a way to add input data
#if sys.argv[1] == 'add':
    #if not sys.argv[2]:
        #inputdetected = input('Please input the to do you want to add:')
        #inputdetected
    #print(f"Input detected : {inputdetected}." )
#else:
    #print('')