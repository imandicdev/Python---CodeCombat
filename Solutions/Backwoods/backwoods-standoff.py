# Munchkins are attacking!
# The swarms will come at regular intervals.
# Whenever you can, cleave to clear the mass of enemies.

while True:
    enemy = hero.findNearestEnemy()
    readytoCleave = hero.isReady("cleave")
    # Use an if-statement with isReady to check "cleave":
    if readytoCleave:
        # Cleave!
        hero.cleave()
    # Else, if cleave is not ready:
    else:
        hero.attack(enemy)
        # Attack the nearest ogre!
        
