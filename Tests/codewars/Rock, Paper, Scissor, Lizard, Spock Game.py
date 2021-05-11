#examples
#"rock", "spock"       -->  "Player 2 won!"      because Spock vaporizes rock
#"scissor", "lizard"   -->  "Player 1 won!"      because scissor decapitates lizard
#"scissor", "Scissor"  -->  "Draw!"              because they are the same
#"foo", "Bar"          -->  "Oh, Unknown Thing"  because they are not valid
import random
import sys

lizard = "lizard"
spock = "spock"
scissor = "scissor"
paper = "paper"
rock = "rock"

a = str(input("lizard, spock, scissor, paper or rock? "))
b = ["lizard", "spock","scissor", "paper", "rock"]
c = random.choice(b)
try:
    a = str(a)
except TypeError:
    print("incorrect type of input")
    sys.exit(0)

def main():
    if a == b[0]:
        print()

main()