#! python3
"""To Do list"""

import sys
import os
import Filedetector
import Loadafile

# Create a nice graphic to display the to do list
# Upgrade the todolist to a dictionnary so that i can contain more info about each task

def main():

    ExistingTodos = []
    ToDolist = []
    number = 1
    def Startscreen():
        print("Please select an argument. \n 1- add \n 2- remove \n 3- exit \n 4- show \n 5- args")    
    print('Welcome to To Do list!')



    # detects files in a folder, then return a list with those files 
    ExistingTodos = Filedetector.detectfiles()

    # load a todo or create a new one
    loadthisfile = Loadafile.loadornewlist(ExistingTodos, ToDolist)

    Startscreen()
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

                # Checks if current filename exits.
                Tosavefile = f'Save{number}.txt'
                while os.path.exists(str(Tosavefile)):
                    number += 1
                    Tosavefile = f'Save{number}.txt'

                # check if it is loading or writing then re-write to the file
                if loadthisfile:
                    with open(loadthisfile, 'w') as f:
                        # TODO: check loadafile.py
                            for i in ToDolist:
                                f.write(str(i))
                                f.write('\n')
                            
                else: 
                    with open(Tosavefile, 'w') as f:
                         for i in ToDolist:
                                f.write(str(i))
                                f.write('\n')
                                
                print('exitting... \n')
                break

        
        elif inputtedCommand == 'show':
            numberoftodos = 0

            if len(ToDolist) == 0:
                print('Your list is empty!')
            
            else:
                for i in range(len(ToDolist)):
                    numberoftodos += 1
                    print(f"{numberoftodos}- {ToDolist[i]}")


        elif inputtedCommand == 'args':
            print('')
            Startscreen()
        

        else:
            print("I'm sorry, i dont understand... \n")



if __name__ == '__main__':
    main()