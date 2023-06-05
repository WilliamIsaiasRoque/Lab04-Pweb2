from interpreter import draw
from chessPictures import *

squarenegative = square.negative() 
squarewhite = squarenegative.negative()
fila = squarewhite.join(squarenegative).horizontalRepeat(4)
filax4=fila.negative().up(fila).verticalRepeat(2)
draw(filax4)