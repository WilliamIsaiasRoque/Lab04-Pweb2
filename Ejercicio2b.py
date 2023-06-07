from interpreter import draw
from chessPictures import *

horse=knight
horseblack=horse.negative()
horse4mirror=horse.join(horseblack).verticalMirror().up(horse.join(horseblack))
draw(horse4mirror)


