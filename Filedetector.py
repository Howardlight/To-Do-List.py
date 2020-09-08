import os


CurrentDirectory = os.getcwd()
def detectfiles():
    ExistingTodos = []
    for _, _, filenames in os.walk(CurrentDirectory):
        for Todos in filenames:
            numberrelatedtofiledetected = 0

            if Todos.lower().endswith(".txt"):
                
                ExistingTodos.append(Todos)
                numberrelatedtofiledetected += 1
                displayfiledetected = os.path.join(CurrentDirectory, Todos)                                             
                print(f'{numberrelatedtofiledetected}: {displayfiledetected}') # NOTE: May need to change these 2                         

        else:
            break

    return ExistingTodos