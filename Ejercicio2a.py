from interpreter import draw
from chessPictures import *

horse=knight
horseblack=horse.negative()
horsewhite=horseblack.negative()

draw(horsewhite.join(horseblack).under(horseblack.join(horsewhite)))


"""
horse = knight
blackHorse = horse.negative()
horses = horse.join(blackHorse)
draw(horses)
"""
"""
horses3 = horse.join(horses)
horses4 = horse.join(horses3)
draw(horses4) """







