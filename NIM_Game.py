import random

def nim_minimal(n): 
    return 1

def nim_best(n):
    taken = n % 4  #div the num by 4 and return the remainder,if remainder is 0 then go to else part
    if taken:
        return taken
    else:
        return random.choice(range(1, min(n,3)+1))

def nim_human1(n):
    while True: #get input until it's legal
        taken = int(input("There are %d sticks. How many do you take? (1/2/3) " %n))
        if taken in range(1, min(n,3)+1):
            return taken
        print("Illegal move.")           

def nim_human2(n):
    while True: #get input until it's legal
        taken = int(input("There are %d sticks. How many do you take? (1/2/3) " %n))
        if taken in range(1, min(n,3)+1):
            return taken
        print("Illegal move.")

def nim_computer(n):
    return random.choice(range(1, 4))
    
    
player_pool = [nim_minimal, nim_best, nim_human1, nim_human2, nim_computer]
player_pool = { p.__name__:p for p in player_pool }

def select_players():
    players = []
    while len(players) < 2:
        print("These are the players: %s" % "/".join(player_pool.keys()))
        p = input("Name one: ")
        if p not in player_pool.keys():
            print("Not a valid player. Select again: ")
            continue
        players.append(p)
    print("Player %s begins, player %s plays second." % tuple(players))
    return players


def game():
    while True:
        n = int(input("Heap size? "))
        if n > 0:
            break #accept only positive numbers
    current, other = tuple(select_players()) #tuple with two elements

#game runs
    while n > 0:
        #as long as there are sticks in the heap
        print("Heap has %d sticks." % n)
        taken = player_pool[current](n) #carry out move; guaranteed legal
        print("%s takes %d sticks.\n" % (current, taken))
        n -= taken #update heap
        current, other = other, current #now it's the other player's turn
    print("%s has lost." % other)


while True: #for continuous game
    game()
