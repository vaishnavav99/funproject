#Stone Paper Scissors game
#Made by Vaishnav A V

import random
array=['rock','paper','scissor']
player=0
computer=0
x='xyz'
while(x!='n'):
    c=(random.choice(array))
    p=input("Player [rock/paper/scissor]:\t ").lower()
    y=p in array
    if(y==True):
        print("computer:\t\t\t",c,"\n")
        if(p==c):
            print("tie \n computer \t player\n",computer,"\t\t",player)
        else:
            if(p=='rock'):
                if(c=='paper'):
                    computer=computer+1
                    print("lose \n computer \t player\n",computer,"\t\t",player)
                else:
                    player=player+1
                    print("won \n computer \t player\n",computer,"\t\t",player)
            if(p=='paper'):
                if(c=='scissor'):
                    computer=computer+1
                    print("lose \n computer \t player\n",computer,"\t\t",player)
                else:
                    player=player+1
                    print("won \n computer \t player\n",computer,"\t\t",player)
            if(p=='scissor'):
                if(c=='rock'):
                    computer=computer+1
                    print("lose \n computer \t player\n",computer,"\t\t",player)
                else:
                    player=player+1
                    print("won \n computer \t player\n",computer,"\t\t",player)
    else:
        print("invalid input")

    x=input("\ndo you want to play again y/n\t").lower()