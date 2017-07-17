from valuetree import ValueTree
from basictree import BasicTree
import random
choiceMode = False
path = ["\npath start"]
totalNodes = 0
debug = 0

Events = dict() # A dictionary of all known trees in a game

gameVars = dict() # A dictionary of all game variables used

def processVars(varEffect):
    """
    processes a 3 part line (string) that controls variables in the gameVars dictionary
    This function also allows the creation of new variables and the addition of
    already defined variables to other variables.

    Args:
        varEffect: a string with three parts: "variable, operator, number/defined variable"
    """
    varEffect = varEffect.split()
    if len(varEffect) == 3: # variable effect line must only contain 3 components
        if varEffect[0] not in gameVars.keys():
            gameVars[varEffect[0]] = 0  # This allows users to define new variables as they modify them

        if varEffect[1] == '+':
            addVar(varEffect[0], varEffect[2])
        elif varEffect[1] == '-':
            subVar(varEffect[0], varEffect[2])
        elif varEffect[1] == '*':
            mulVar(varEffect[0], varEffect[2])
        elif varEffect[1] == '/':
            divVar(varEffect[0], varEffect[2])
        elif varEffect[1] == '=':
            setVar(varEffect[0], varEffect[2])
        else:
            raise SyntaxError ('"{}" is not a valid operator'.format(varEffect[1]))

def addVar(var, num):
    """Adds the value of var and a given num then saves the result as the
    new value of var.

    Args:
        var: a key in gameVars
        num: a string representing an int or a key in gameVars
    """
    if num.isdigit():
        gameVars[var] += int(num)
    elif num in gameVars.keys():
        gameVars[var] += gameVars[num]
    else:
        raise KeyError ("{} is not a variable in the game".format(num))

def subVar(var, num):
    """Subtracts the value of var from a given num then saves the result as the
    new value of var.

    Args:
        var: a key in gameVars
        num: a string representing an int or a key in gameVars
    """
    if num.isdigit():
        gameVars[var] -= int(num)
    elif num in gameVars.keys():
        gameVars[var] -= gameVars[num]
    else:
        raise KeyError ("{} is not a variable in the game".format(num))

def mulVar(var, num):
    """Multiplies the value of var and a given num then saves the result as the
    new value of var.

    Args:
        var: a key in gameVars
        num: a string representing an int or a key in gameVars
    """
    if num.isdigit():
        gameVars[var] *= int(num)
    elif num in gameVars.keys():
        gameVars[var] *= gameVars[num]
    else:
        raise KeyError ("{} is not a variable in the game".format(num))

def divVar(var, num):
    """Divides the value of var by a given num then saves the result as the
    new value of var.

    Args:
        var: a key in gameVars
        num: a string representing an int or a key in gameVars
    """
    if num.isdigit():
        gameVars[var] /= int(num)
    elif num in gameVars.keys():
        gameVars[var] /= gameVars[num]
    else:
        raise KeyError ("{} is not a variable in the game".format(num))

def setVar(var, num):
    """Sets the value of var to a given num.

    Args:
        var: a key in gameVars
        num: a string representing an int or a key in gameVars
    """
    if num.isdigit():
        gameVars[var] = int(num)
    elif num in gameVars.keys():
        gameVars[var] = gameVars[num]
    else:
        raise KeyError ("{} is not a variable in the game".format(num))

def processCondition(condition):
    """
    processes a 3 part line (string) then checks whether an already defined game
    variable meets the condition or not.

    Args:
        condition: a string with three parts:
            "defined variable, operator, number/defined variable"

    Returns (bool) True or False based on the condition.
    """
    global debug
    condition = condition.split()
    if len(condition) == 3: # condition line must only contain 3 components
        if condition[0] not in gameVars.keys():
            raise KeyError ("variable {} has not been defined".format(condition[0]))
        else:
            var = gameVars[condition[0]]
        if not condition[2].isdigit():
            if condition[2] not in gameVars.keys():
                raise KeyError ("variable {} has not been defined".format(condition[2]))
            else:
                num = gameVars[condition[2]]
        else:
            num = int(condition[2])

        debug and print(condition)

        if condition[1] == '>':
            if var > num:
                return True
        elif condition[1] == '>=':
            if var >= num:
                return True
        elif condition[1] == '<':
            if var < num:
                return True
        elif condition[1] == '<=':
            if var <= num:
                return True
        elif condition[1] == '=':
            if var == num:
                return True
        else:
            raise SyntaxError ('"{}" is not a valid operator'.format(condition[1]))
        return False


def identifyNodetype(tree):
    """Identifys node type of tree then runs the function associated with the
    identified event type. The function is called again on the returned tree.

    Args:
        tree: a ValueTree

    Returns: zero if an error occurs.
    """
    global debug
    global gameVars
    print()
    debug and print(gameVars)
    v = tree.get_value()

    if v[1] == 'S':
        tree = runSimple(v, tree)
    elif v[1] == 'P':
        if choiceMode == True:
            #alows player to chose the path they go on
            tree = runChoice(v, tree)
        else:
            tree = runProbability(v, tree)
    elif v[1] == 'C':
        tree = runConditional(v, tree)
    elif v[1] == 'R':
        tree = runRandom(v, tree)
    elif v[1] == 'E':
        tree = runEnd(v, tree)
    else:
        raise SyntaxError ("Nodetype: {} not applicable".format(v[1]))
    if tree == 0:
        #end the game
        return 0
        quit()
    if type(tree) is str:
        global Events
        tree = Events[tree]

    identifyNodetype(tree)

def runSimple(v, tree):
    "Run a simple event and return the selected child tree"
    ch = tree.get_children()
    processVars(v[3])
    print (v[2])

    path.append(v[2])

    response = input()
    path.append(response)

    # if user presses enter assume option 1
    if len(response) == 0:
        newtree = ch[0]
        return newtree

    # checks if the response is approperiate
    if response.isdigit():
        if int(response) < len(ch)+1:
            newtree = ch[int(response)-1]
            return newtree

    print("Invalid input. Try again")
    runSimple(v, tree)


def runChoice(v, tree):
    '''if choiceMode is on then the player can direct their path without
    regard for probability'''
    ch = tree.get_children()
    processVars(v[3])
    print (v[2],"\n")
    path.append(v[2])
    print("choiceMode is activated, do you choose \n1 - 'pass' or \n2 - 'fail'")
    response = int(input())

    if response == 1:
        newtree = ch[0]
        path.append("pass")
    elif response == 2:
        newtree = ch[1]
        path.append("fail")
    return newtree

def runProbability(v, tree):
    """Runs the probabilty event then selects a new tree based on the probability
    provided in the value of that node"""
    global debug
    path.append(v[2])
    ch = tree.get_children()
    processVars(v[3])
    outcome = random.randrange(100)
    debug and print(outcome)
    if outcome <= v[4]:
        newtree = ch[0]
        path.append("pass")
    else:
        newtree = ch[1]
        path.append("fail")
    return newtree

def runConditional(v, tree):
    "Runs the conditional event then returns child tree based on the condition"
    ch = tree.get_children()
    processVars(v[3])
    if len(v[2]) != 0:
        print (v[2])
        input() # just an ENTER for user confirmation

    path.append(v[2])
    if processCondition(v[4]):
        newtree = ch[0]
    else:
        newtree = ch[1]
    return newtree

def runRandom(v, tree):
    "Runs the random event by selecting a new tree randomly from the children"
    ch = tree.get_children()
    processVars(v[3])
    print(v[2])
    path.append(v[2])
    outcome = random.randrange(len(ch))
    path.append("outcome: " + str(outcome))
    newtree = ch[outcome]
    return newtree

def runEnd(v, tree):
    "Runs the end event and returns zero"
    print(v[2])
    path.append(v[2])
    #return 0 to signify end of game
    return 0


def create():
    "This is the main function that creates a game"
    global debug
    global Events
    print ("""\nHello! You are building an adventure from scratch!""")
    print ("""Would you like to save your created game?\n1. yes\n2. no""")
    save = int(input())

    if save == 1:
        filename = input("\nPlease specifiy a file name:  ")
        File = open(filename, 'w')
    else:
        File = 0 # File will only be zero if user does not want to save created game

    print("\nNote: If you'd like to load a game already made and saved through this program then just copy and paste the contents of the saved file right now.")

    tree = createEvent(File)

    if File:
        File.close()

    debug and print(Events)
    print("\nYour game is now complete.\nYou will be redirected to the main menu where you can choose option 2 to play your game.")
    main(tree)
    return tree


def createEvent(File):
    """
    This is a recursing function that returns multiple ValueTrees nested
    together.

    Args:
        File: the file to store the inputs, otherwise File = 0

    Returns (ValueTree)
    """
    global debug
    global totalNodes
    global Events
    print()
    debug and print(Events)
    print ("""You are creating an event""")
    preDefined = input("If you wish to use a pre-existing event give the ID:  ")
    if File:
        File.write(preDefined+"\n")
    if len(preDefined) > 0:
        return preDefined

    totalNodes+=1
    nodeID = ("ID#"+str(totalNodes))
    print("Event ID:  {}".format(nodeID))

    nodetype = input("What is your event type?  ")
    prompt = input("What is your prompt?  ")
    if File:
        File.write(nodetype+"\n"+prompt+"\n")
    childrenTemp = []

    # End Event
    if nodetype == 'E':
        Events[nodeID] = ValueTree(value = [nodeID, nodetype, prompt])
        return ValueTree(value = [nodeID, nodetype, prompt])

    varEffect = input("Does this event have an effect on a variable?  ")

    # Simple Event
    if nodetype == 'S':
        outcomeNum = int(input("How many outcomes do you want this event to have?  "))
        if File:
            File.write(varEffect+"\n"+str(outcomeNum)+"\n")
        for i in range(outcomeNum):
            print()
            print ("""Your last prompt was:\n     {}""".format(prompt))
            option = input("What is Your option #{}?  ".format(i+1))
            if File:
                File.write(option+"\n")
            prompt += "\n     {}. {}".format(i+1, option)
            childrenTemp.append(createEvent(File))
        Events[nodeID] = ValueTree(value = [nodeID, nodetype, prompt, varEffect], children = childrenTemp)
        return ValueTree(value = [nodeID, nodetype, prompt, varEffect], children = childrenTemp)

    # Probability Event
    elif nodetype == 'P':
        for i in range(2):
            print()
            if i == 0:
                prob = int(input("""What are the chances that outcome #{} occurs? (out of 100):  """.format(i+1)))
                if File:
                    File.write(varEffect+"\n"+str(prob)+"\n")
            childrenTemp.append(createEvent(File))
        Events[nodeID] = ValueTree(value = [nodeID, nodetype, prompt, varEffect, prob], children = childrenTemp)
        return ValueTree(value = [nodeID, nodetype, prompt, varEffect, prob], children = childrenTemp)

    # Conditional Event
    elif nodetype == 'C':
        for i in range(2):
            print()
            if i == 0:
                condition = input("What is the condition for the first outcome?  ")
                print ("""Your last prompt was:\n     {}""".format(prompt))
                print("You will now define the 'True' condition event:")
                if File:
                    File.write(varEffect+"\n"+condition+"\n")
            else:
                print ("""Your last prompt was:\n     {}""".format(prompt))
                print("You will now define the 'False' condition event:")
            childrenTemp.append(createEvent(File))
        Events[nodeID] = ValueTree(value = [nodeID, nodetype, prompt, varEffect, condition], children = childrenTemp)
        return ValueTree(value = [nodeID, nodetype, prompt, varEffect, condition], children = childrenTemp)

    # Random Event
    elif nodetype == 'R':
        outcomeNum = int(input("How many outcomes do you want this event to have?  "))
        if File:
            File.write(varEffect+"\n"+str(outcomeNum)+"\n")
        for i in range(outcomeNum):
            print()
            childrenTemp.append(createEvent(File))
        Events[nodeID] = ValueTree(value = [nodeID, nodetype, prompt, varEffect], children = childrenTemp)
        return ValueTree(value = [nodeID, nodetype, prompt, varEffect], children = childrenTemp)

    else:
        raise SyntaxError ("Nodetype: {} not applicable".format(nodetype))

def runpath():
    '''Displays path to user in colour'''
    W  = '\033[0m'  # white (normal)
    R  = '\033[31m' # red
    G  = '\033[32m' # green
    O  = '\033[33m' # orange
    B  = '\033[34m' # blue
    P  = '\033[35m' # purple
    for i in range(len(path)):
        if i == 0:
            print(G+ path[i] +P)
        elif i == len(path) - 1:
            print(G+ path[i] +W)
        else:
            print(path[i])


def main(tree):
    '''Runs the game user input'''
    global path
    global choiceMode
    global gameVars
    gameVars = dict()

    print("\nWelcome to the tree game generator \n 1 - Create/load new game \n 2 - Play loaded game (if no game is loaded demo game will play) \n 3 - Quit")
    yes = int(input())
    if yes == 1:
        #create a game
        tree = create()
        return tree

    elif yes == 2:
        #Play the demmo game
        print("\nTurn on choiceMode? \n 1 - yes \n 2 - no")
        yes = int(input())
        if yes == 1:
            choiceMode = True

        #play game
        identifyNodetype(tree)
        path.append("\npath end.\n")

        print("\nSee path? \n 1 - yes \n 2 - no")
        yes = int(input())
        if yes == 1:
            runpath()

        print("\nClear path? \n 1 - yes \n 2 - no")
        yes = int(input())
        if yes == 1:
            path = ["\npath start"]

    elif yes == 3:
        quit()


if __name__ == "__main__":
    from demo import demo
    tree = demo()
    while True:
        tree = main(tree)
        print("\nReturn to main menu? \n 1 - yes \n 2 - no")
        yes = int(input())
        if yes == 2:
            #exit program
            print("\nGoodbye.")
            break
