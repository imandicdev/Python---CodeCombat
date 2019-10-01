# Move to 'Laszlo' and get his secret number.
hero.moveXY(30, 13)
laszlo = hero.findNearestFriend().getSecret()

# Add 7 to 'Laszlo's number to get 'Erzsebet's number.
# Move to 'Erzsebet' and say her magic number.
erzsebet = laszlo + 7
hero.moveXY(17, 26)
hero.say(erzsebet)

# Divide 'Erzsebet's number by 4 to get 'Simonyi's number.
# Go to 'Simonyi' and tell him his number.
simonyi = erzsebet / 4;
hero.moveXY(30, 39)
hero.say(simonyi)
# Multiply 'Simonyi's number by 'Laszlo's to get 'Agata's number.
# Go to 'Agata' and tell her her number.
agata = simonyi * laszlo;
hero.moveXY(43, 26)
hero.say(agata)
