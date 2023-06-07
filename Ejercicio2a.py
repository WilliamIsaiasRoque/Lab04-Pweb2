from interpreter import draw
from chessPictures import *

horse=knight
horseblack=horse.negative()
horse4=horseblack.join(horse).up((horse).join(horseblack))
draw(horse4)








