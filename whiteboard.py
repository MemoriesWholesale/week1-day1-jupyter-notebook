# Oh Noes!!! The score keeper never showed up at our Cricket game!
# No one knows how to keep score!
# Since the game must continue, but the players don't know how to score the game;
# They decided each player would take no more than 20 tries (alternating with their opponent)
# Each try would consist of 3 throws.  
# They end up making two lists one for each player and just write down the number
# each player hit and postfix it with whether they hit a single [s] double [d]
# triple [t].  If they miss the board completely it will be written as a "0s" 
# if they hit a double 20 it would be written "20d" or a triple three 
# would be "3t".  The Bulleyes will be represented as "b" and double bullseye
# would be "bd".  
#
# They have given you the tallies and need you to determine the winner.
# Sometimes there might not be a winner as they only played 20 rounds.
# Write a function to take the lists created and determine a winner.
# If player 1 wins return "Player 1 Wins" if player 2 wins 
# return "Player 2 Wins" if no one wins return "Incomplete"  
#
# Player 1 list will always been given first and Player 1 
# also starts every game.
# Both players will always have the same number of throws


# Create Scoreboards for each player
# Score the rounds in groups of 3 throws adding the score to the scoreboard for each throw
# after checking each player's turn check to see if that player has won
# Tally scores until a winner is determined and return "Player (1/2) wins"
# if no winner is determined than return "Incomplete"

def solution(p1_throws, p2_throws):
    p1_scoreboard = {'20': 0, '19': 0, '18': 0, '17': 0, '16': 0, '15': 0, 'b': 0}
    p2_scoreboard = {'20': 0, '19': 0, '18': 0, '17': 0, '16': 0, '15': 0, 'b': 0}
    number_of_throws = len(p1_throws)

    for i in range(0, number_of_throws, 3):
        for throw in p1_throws[i:i+3]:
            if throw[0:-1] not in p1_scoreboard:
                continue
            multiplier = 0
            if throw[-1]  == 's':
                multiplier = 1
            elif throw[-1] == 'd':
                multiplier = 2
            elif throw[-1] == 't':
                multiplier = 3
            p1_scoreboard[throw[0:-1]] += multiplier

            count_closed = 0
            for shot in p1_scoreboard.values():
                if shot >= 3:
                    count_closed += 1
            if count_closed >= 7:
                return 'Player 1 Wins'
            
        for throw in p2_throws[i:i+3]:
            if throw[0:-1] not in p2_scoreboard:
                continue
            multiplier = 0
            if throw[-1]  == 's':
                multiplier = 1
            elif throw[-1] == 'd':
                multiplier = 2
            elif throw[-1] == 't':
                multiplier = 3
            p2_scoreboard[throw[0:-1]] += multiplier

            count_closed = 0
            for shot in p2_scoreboard.values():
                if shot >= 3:
                    count_closed += 1
            if count_closed >= 7:
                return 'Player 2 Wins'
            
    return 'Incomplete'

