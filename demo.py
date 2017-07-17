# tree templates:
# tree =  ValueTree(value = ['S', """Do you:
# \n 1 -
# \n 2 - """])
# tree = ValueTree(value = ['E', """"""])
# tree =  ValueTree(value = ['R', """"""])
# tree = ValueTree(value = ['P', """""", 10 ])
from valuetree import ValueTree
from basictree import BasicTree
import TreeQuest

def demo():
    #retturns tree that contains demmo game

    checkResults = ValueTree(value=["", 'C', """Your journey has come to an end.
Let's see how good of a person you've been. (press ENTER to continue)""", "", "good < 0"])
    checkAgain = ValueTree(value=["", 'C', "", "", "good > 0"])
    bad = ValueTree(value=["", 'E', 'You have a "good" score bellow zero! You\'re a terrible person!'])
    neutral = ValueTree(value=["", 'E', 'You have a "good" score of zero. How sustainable!'])
    good = ValueTree(value=["", 'E', 'You have a positive "good" score. Eyy that\'s pretty good!'])

    checkResults.set_children([bad, checkAgain])
    checkAgain.set_children([good, neutral])


    treeQuest = ValueTree(value = ["",'S', """You are falling from a tree, do you:
    \n1 - attempt a magnificent feat of acrobatics in order to land safely? or
    \n2 - swing on a nearby vine to safety""", ""])

    tree1 = ValueTree(value = ["", 'P', "", "good = 0", 10, ])
    tree2 = ValueTree(value = ["", 'S', """You swing onto a nearby cliff safely however,
the weak vine rips from the tree and lies dead in a pool of its own vine juices.
How dare you! (good - 5).
You are currently surounded by an eerie fog. Do you:
    \n1 - Climb down the cliff to the forest below? or
    \n2 - set out into the fog""", "good - 5"])
    treeQuest.set_children([tree1, tree2])      #Fixed up to this point

    underworld1 = ValueTree(value = ["", 'S', """You fail miserably and crash to the ground...
    \nYou're Dead. (demo end)""", ""])
    underworld1.set_children([checkResults])
    tree4 = ValueTree(value = ["", 'S', """You've made it  safely to the ground, A great forest
stretches out before you. Do you
    \n 1 - climb another tree and gather your bearings? or
    \n 2 - Just start walking in some direction?""", ""])
    tree1.set_children([underworld1, tree4])

    tree5 = ValueTree(value = ["", 'R', """You'll make it out eventually right?""", ""])
    tree2.set_children([tree4, tree5])

    tree6 = ValueTree(value = ["", 'S', """You see a castle not far south from you. Do you:
    \n 1 - Make your way over to it? or
    \n 2 - Flee in the opposite direction, lest the authority's catch you?""", ""])
    tree7 =  ValueTree(value = ["", 'R', """The forest is dense and you have a
    hard time finding your way.""", ""])
    tree4.set_children([tree6, tree7])

    tree8 =  ValueTree(value = ["", 'S', """You find your way to a castle. While old, It looks
well maintained; some one should be living inside, Do you:
    \n 1 - Knock on the door, and ask for help? or
    \n 2 - Sneek inside?""", ""])
    tree9 = ValueTree(value = ["", 'P', "No way are you letting yourself get thrown in a dungon! (good + 5)", "good + 5", 30 ])
    tree6.set_children([tree8, tree9])

    tree10 =  ValueTree(value = ["", 'S', """The massive door before you opens and an
old man greets you,
    \n\Old Man: "what business do you have here?\"You reply:
    \n 1 - \"[lie] I got lost in the forest on the way to my grandmother's and
came here looking for help.\"
    \n 2 - [lie?] \"I come bearing gifts!\"
    \n 3 - \"Well actually... A giant bird kidnaped me and when I tried to escape
I fell from it's nest. I came to this castle hoping someone could tell me
where I am.... ha haa...\" [hope the old man doesn't know who the bird
belongs to] """, ""])
    tree11 = ValueTree(value = ["", 'P', """You slip inside through an unlatched window.
A breaking and entering?! What a criminal! (good - 10)""", "good - 10", 50 ])
    tree8.set_children([tree10, tree11])

    tree12 = ValueTree(value = ["", 'S', """get caught (demo end)""", ""])
    tree12.set_children([checkResults])
    tree13 = ValueTree(value = ["", 'S', """sneak in safely (demo end)""", ""])
    tree13.set_children([checkResults])
    tree11.set_children([tree12, tree13])

    tree14 = ValueTree(value = ["", 'P', """Well, you are lost, but you also have no grandmother to
speak of... lets hope the old man focuses on the lost part (good - 1)""", "good - 1", 55 ])
    tree15 = ValueTree(value = ["", 'P', """It's not a lie that you have a gift, The golden feather
you grabbed out of that birds nest will do just fine, You just hope the old
man doesn't pry too deeply (good - 1)""", "good - 1", 70])
    tree16 = ValueTree(value = ["", 'S', """You tell the truth (good + 5).
    \"Sounds like you've had quite the
journey, come inside and tell me more. You:
    \n 1 - Follow the man inside taking note of your suroundings
    \n 2 - Turn tail and run! It's not worth the risk after all.""", "good + 5"])
    tree10.set_children([tree14, tree15, tree16])

    tree17 =  ValueTree(value = ["", 'S', """The man leads you down stone coridors lined with all manner
of expensive furniture and art, all looking centuries old. Finaly he leads you into a sitting
room and you settle down and a chair near the fireplace. He sits down across form you.
Old Man: \"I Know who that bird belongs to.\" You:
    \n 1 - stay silent
    \n 2 - interupt: \"It's not what it looks like, I mean yeah that bird caught me
escaping the kings castle but If you let me explain!\" """, ""])
    tree18 =  ValueTree(value = ["", 'R', """Who knows how far those wanted posters have
reached? better to take your chances in the forest""", ""])
    tree16.set_children([tree17, tree18])

    tree19 = ValueTree(value = ["", 'S', """Old Man \"That's a nice story, too bad I've already seen the
posters.\"The old man snaps a pair of hand cuffs on you, you are captured! (demo end)""", ""])
    tree19.set_children([checkResults])
    tree14.set_children([tree17, tree19])
    tree15.set_children([tree17, tree19])

    tree20 = ValueTree(value = ["", 'S', """Old Man: \"And I have no love for that man either,
maybe we can work something out\" (demo end) """, ""])
    tree20.set_children([checkResults])
    tree21 = ValueTree(value = ["", 'S', """Old Man: \"Do you really plan on going on with this, or do you
want to hear aboout all the ways I can help you? (demo end)\" """, ""])
    tree21.set_children([checkResults])
    tree17.set_children([tree20, tree21])


    underworld2 = ValueTree(value = ["", 'S', """You have arrived to The underworld
however this seems like a lot to program therefore the demo has come to an end. You should
play again and see what else you can find. (demo end)""", ""])
    underworld2.set_children([checkResults])
    creepy1 = ValueTree(value = ["", 'S', """The forest around you is dark and foreboding, no doubt
the shadows hide evil, can you make it out alive? (demo end)""", ""])
    creepy1.set_children([checkResults])
    enchated1 = ValueTree(value = ["", 'S', """The forest around you feels strange, like something
is not quite right. Wait... haven't you seen that tree before!(demo end)""", ""])
    enchated1.set_children([checkResults])
    exit1 = ValueTree(value = ["", 'S', """exit1""", ""])
    exit1.set_children([checkResults])
    tree7.set_children([creepy1, enchated1, exit1, underworld2])
    tree5.set_children([creepy1, underworld2])
    tree9.set_children([exit1, creepy1])
    tree18.set_children([creepy1, enchated1, exit1])

    return treeQuest

# Run the demo
