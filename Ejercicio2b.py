from interpreter import draw
from chessPictures import *

horse=knight
horseblack=horse.negative()
horsewhite=horseblack.negative()
horse4mirror=horsewhite.join(horseblack).horizontalMirror().up(horsewhite.join(horseblack))

draw(horse4mirror)


