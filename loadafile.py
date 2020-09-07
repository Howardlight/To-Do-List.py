import os

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
                        loadthisfile = os.path.join('D:/Projects/TodoList Python', str(ExistingTodos[selectloadfileinput]))
                        with open(loadthisfile, 'r') as loadedfile:
                            for line in loadedfile:
                                # TODO: figure out a way to delete the '\n' from the end of each todo string
                                #if line.endswith('\n'):
                                    #newline = line.
                                ToDolist.append(line)
                        break
                    break
                break


        elif Loadorcreate == 'n':
            loadthisfile = False
            break 

    return loadthisfile