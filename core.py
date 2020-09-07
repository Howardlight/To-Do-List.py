#! python3
"""To Do list"""

import sys
import os
import Detectfileindir
import loadafile

# Branch the code out into multiple files IE make it tidy
# Create a nice graphic to display the to do list
# Make the to do list CMD compatible
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

    # detects files in a folder, then return a list with those files 
    ExistingTodos = Detectfileindir.detectfiles()

    # load a todo or create a new one
    loadthisfile = loadafile.loadornewlist(ExistingTodos, ToDolist)

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
                # TODO: allow the user to name the txt? [very easy to implement]

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
                            # f.write('\n'.join([''.join(i) for i in ToDolist]))
                else: 
                    with open(Tosavefile, 'w') as f:
                         for i in ToDolist:
                                f.write(str(i))
                                f.write('\n')
                        # f.write('\n'.join([''.join(i) for i in ToDolist]))

                break

        
        # TODO: when activated, list contains spaces for some reason, fix this
        elif inputtedCommand == 'show':
            numberoftodos = 0
            # TODO: add a gate for when the list is empty
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