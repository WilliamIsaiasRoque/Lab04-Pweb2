from interpreter import draw
from chessPictures import *

horse=knight
horseblack=horse.negative()
horsewhite=horseblack.negative()
horse4=horseblack.join(horsewhite).up((horsewhite).join(horseblack))

draw(horse4)








