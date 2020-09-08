import os
from Filedetector import CurrentDirectory

def loadornewlist(ExistingTodos, ToDolist):
    print('')
    Loadorcreate = input('Would you like to load a todo list or create a new one? (l/n)')
    while True:
        if Loadorcreate == 'l':

            if len(ExistingTodos) <= 0:
                print('There are no todos in your directory!')
                loadthisfile = False
                return loadthisfile

            else:

                for file in ExistingTodos:
                    print(file)
            

                while True:
                    selectloadfileinput = int(input('which file would you like to open ?'))  - 1

                    if selectloadfileinput > len(ExistingTodos) or selectloadfileinput <= -1:
                        print('That file does not exist! \n')

                    else:
                        loadthisfile = os.path.join(CurrentDirectory, str(ExistingTodos[selectloadfileinput]))
                        with open(loadthisfile, 'r') as loadedfile:
                            for line in loadedfile:

                                if line.endswith('\n'):
                                    strippedline = line.rstrip('\n')
                                    ToDolist.append(strippedline)

                                else:
                                    ToDolist.append(line)
                        break
                    break
                break


        elif Loadorcreate == 'n':
            loadthisfile = False
            break 

    return loadthisfile