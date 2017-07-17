# TextGameMaker
A tool for creating text based game in which players make choices based on a given prompt

Sundus Mahdi and Zoe Downton
CMPUT 275

For our project we created a program that allows users to create their own
tree-structured adventure game through the terminal.

To use the program run the file TreeQuest.py then follow the prompts and make
your selections by entering the approperiate numbers.



The tree game generator has 5 different event types defined below:

end (E):
    a ValueTree that has no children and specifies the end of the game.

    value = [nodeID(str), nodetype(str), prompt(str)]
    children = []

simple (S):
    A ValueTree that must have one or more children. The child tree that is used
    is determined by player input.

    value = [nodeID(str), nodetype(str), prompt(str), varEffect(str)]
    children = list of 1 or more ValueTrees

probability (P):
    A ValueTree with two children. The child tree that is used is determined by
    random chance depending on the percentage of likeliness for the first event
    to occur (5th paramater in values).

    value = [nodeID(str), nodetype(str), prompt(str), varEffect(str), percent(int)]
    children = list of 2 ValueTrees (success tree and fail tree)

random (R):
    A ValueTree that must have one or more children. The child tree that is used
    is determined randomly (where each child is equally likely yo be chosen) and
    not by player input.

    value = [nodeID(str), nodetype(str), prompt(str), varEffect(str)]
    children = list of 1 or more ValueTrees

conditional (C):
    A ValueTree with two children. The child tree that is used is determined by
    the condition (5th paramater in values) which uses the first child if satisfied.

    value = [nodeID, nodetype, prompt, varEffect, condition]
    children = list of 2 ValueTrees (True tree and False tree)



Here's a walkthough of the more confusing prompts:

While creating a game:
"If you wish to use a pre-existing event give the ID: "
    If you notice, each event has a marking ID that appears in another prompt
    for example:
        "Event ID:  ID#1"
    This basically asks if you want to reuse a defined tree then give
    the ID (ID#1) or you can leave it blank and it will continue normally.

"What is your event type?"
    This asks which of the five events defined above you would like to use.
    Your answer must be one letter and uppercase (either: E, S, P, R, or C).

"What is your prompt?"
    This is the text that will be displayed to the player when they reach
    that event.

"Does this event have an effect on a variable?"
    This line asks if you want to modify a game variable. Inputs must be 3
    seperate words and consist of "variable operator number" or
    "variable operator predefined-variable". The modefied variable does not
    have to be already defined. However, if you do not want to modify a
    variable just leave the line empty.
    Examples:
        good + 10
        luck / 50
        health - attack

    For more information visit the function responsible for this on line 49.

"What is the condition for the first outcome?"
    This line is mandatory and must be filled. Inputs must be 3 seperate
    words and consist of "predefined-variable operator number" or
    "predefined-variable operator predefined-variable".
    Examples:
        good > bad
        health <= 0
        coins = 100

    For more information visit the function responsible for this on line 116.

While running a game:
"Turn on choiceMode?"
    This allows player to choose whether they would like to player
    through the pass or fail trees rather than leave it to blind luck
    when encountering a probability event. It was added for debugging
    but we figured it would be fine to leave it in just for the
    completionists in all of us.

"See path?"
    This is the equivalent of an instant replay. It reprints your chosen
    path for you to see.

"Clear path?"
    If selected this will delete your saved "instant replay" otherwise
    all your games from that session will be saved into one large path.


To try loading a premade game copy the contents of the file loop to the
program once the first "If you wish to use a pre-existing event give the ID: "
appears.
