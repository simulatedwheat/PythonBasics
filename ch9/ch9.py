# Chapter 9, Simulation and Design.
from random import random

# Raquetball simulation
def raquetball():
    print_intro()
    prob_a, prob_b, n_games = getInputs()
    wins_a, wins_b, shutouts_a, shutouts_b = simulate_games(n_games, prob_a, prob_b)
    print_summary(wins_a, wins_b, shutouts_a, shutouts_b)


def print_intro():
    print("""This program is a simulation of a raquetball game with 
the two players having probabilities of winning each serve (0-1).
It takes the probabilities and the number of games as input.""")
    
def getInputs():
    # Returns the three simulation parameters
    a = float(input("What is the probability that player A wins a serve? "))
    b = float(input("What is the probability that player B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n

def simulate_games(n_games, prob_a, prob_b):
    # Simulates n games and returns wins_a and wins_b
    wins_a = 0
    wins_b = 0
    shutouts_a = 0
    shutouts_b = 0
    for i in range(n_games):
        score_a, score_b, shutouts_A, shutouts_B = sim_one_game(prob_a, prob_b)
        if score_a > score_b:
            wins_a = wins_a + 1
        else:
            wins_b = wins_b + 1 
        if shutouts_A > 0:
            shutouts_a = shutouts_a + 1
        if shutouts_B > 0:
            shutouts_b = shutouts_b + 1
    return wins_a, wins_b, shutouts_a, shutouts_b

def sim_one_game(prob_a, prob_b):
    score_a = 0
    score_b = 0
    shutouts_a = 0
    shutouts_b = 0
    serving = "A"
    while not game_over(score_a, score_b):
        if serving == "A":
            # A wins the serve
            if random() < prob_a:
                score_a = score_a + 1
            # A loses the serve
            else:
                serving = "B"
        else:
            # B wins the serve
            if random() < prob_b:
                score_b = score_b + 1
            # B loses the serve
            else:
                serving = "A"
    if score_a == 11 and score_b == 0:
        shutouts_a = shutouts_a + 1
    if score_b == 11 and score_a == 0:
                shutouts_b = shutouts_b + 1

    return score_a, score_b, shutouts_a, shutouts_b

def game_over(a, b):
    # a and b represents scores from a game
    # Returns true if the game is over
    return a == 15 or b == 15 or a == 11 or b == 11

def print_summary(wins_a, wins_b, shutouts_a, shutouts_b):
    # Prints a summary of wins for each player
    n = wins_a + wins_b
    shutouts_tot = shutouts_a + shutouts_b
    print("\nGames Simulated:", n)
    print("Wins for A: {0} ({1:0.1%})".format(wins_a, wins_a/n))
    print("Shutouts for A:", shutouts_a)
    print("Wins for B: {0} ({1:0.1%})".format(wins_b, wins_b/n))
    print("Shutouts for B:", shutouts_b)
    print("Shutout Wins: {0} ({1:0.1%})".format(shutouts_tot, shutouts_tot/ n))



# if __name__ == '__main__': is used 
# to execute some code 
# only if the file was run 
# directly, and not imported
if __name__ == '__main__':
    raquetball()


# #8, #9, looks fun