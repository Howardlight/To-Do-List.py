#! python3
"""To Do list"""



import sys

# make a list or dictionnary that contains the to do list
# find a way to save the to do list
# find a way to display the to do list
# find a way to add and delete items from the to do list

ToDolist = []
numberoftodos = 0
LenghofToDolist = len(ToDolist)

# argnumber = len(sys.argv)
# argparsed = str(sys.argv)
# argslengh = len(sys.argv)
args = sys.argv


print('Welcome to To Do list! \nPlease select an argument. \n 1- add \n 2- remove \n 3- exit \n 4- show')
while True:
    inputtedCommand = input('>> ')


    if inputtedCommand == 'add':
        newTodo = input('Please input your new todo >> ')
        ToDolist.append(newTodo)
        print(f'Added "{newTodo}" to your Todo list!')


    if inputtedCommand == 'remove':

        if len(ToDolist) <= 0:
            print('Your to do list is empty. \n')

        else:
            while True:

                tododelete = input(f"""Please select which todo you want to remove \n{str(ToDolist)} \ntype 'cancel' to cancel \n>> """)


                if tododelete == 'cancel':
                    print('Cancelling.. \n\nPlease select an argument. \n 1- add \n 2- remove \n 3- exit \n 4- show')
                    break
                
                elif str(tododelete):
                    print("I'm sorry, i dont understand...")

                elif int(tododelete):

                    if int(tododelete) > len(ToDolist):
                        print('That todo does not exist!')

                    else:
                        print(f'Deleting {ToDolist[(int(tododelete) - 1)]} from your todo list...')
                        ToDolist.pop(int(int(tododelete) - 1))
                        print('Item Deleted! \n')
                
                
                    
                        



    if inputtedCommand == 'exit':
            # add an auto save function
            print('exitting... \n')
            break


    if inputtedCommand == 'show':
        for i in range(len(ToDolist)):
            numberoftodos += 1
            print(f"{numberoftodos}- {ToDolist[i]}")
    

    # TO BE ADDED #
    #else:
        #print("I'm sorry, i dont understand... \n")

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