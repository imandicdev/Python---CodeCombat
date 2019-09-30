# Go to the end of the path and build a fence on the X
# Use your moveXY(x, y) function.

# It's the first point of the path.
hero.moveXY(36, 59)
# Move at the next points of the path.
hero.moveXY(37, 13)
hero.moveXY(56, 17)
hero.moveXY(72, 25)
hero.moveXY(71, 20)
# Build a fence to stop the ogre.
hero.buildXY("fire-trap", 71, 25) # fire trap seems better idea so it kills Ogre and makes a path clean to another 2 gems
hero.moveXY(56, 17)
hero.moveXY(74, 59)
