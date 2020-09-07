import os


def detectfiles():
    # TODO: change dir, so that it automatically loads directory of the script.
    ExistingTodos = []
    for folderName, subfolders, filenames in os.walk("D:/Projects/TodoList Python"):
        for Todos in filenames:
            numberrelatedtofiledetected = 0

            if Todos.lower().endswith(".txt"):
                
                ExistingTodos.append(Todos)
                numberrelatedtofiledetected += 1
                displayfiledetected = os.path.join('D:/Projects/TodoList Python', Todos)                                             
                print(f'{numberrelatedtofiledetected}: {displayfiledetected}') # NOTE: May need to change these 2                         

        else:
            break

    return ExistingTodos