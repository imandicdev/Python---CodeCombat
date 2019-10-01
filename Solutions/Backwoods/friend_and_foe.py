# Peasants and peons are gathering in the forest.
# Command the peasants to battle and the peons to go away!

while True:
    friend = hero.findNearestFriend()
    if friend:
        hero.say("To battle, " + friend.id + "!")
    # Now find the nearest enemy and tell them to go away
    enemy = hero.findNearest(hero.findEnemies())
    if enemy:
        hero.say("Go away, " + enemy.id + "!")
