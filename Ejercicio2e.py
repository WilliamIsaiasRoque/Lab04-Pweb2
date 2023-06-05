from interpreter import draw
from chessPictures import *

squarenegative = square.negative() 
squarewhite = squarenegative.negative()
fila = squarenegative.join(squarewhite).horizontalRepeat(4)

draw(fila)